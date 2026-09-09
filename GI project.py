import pandas as pd

# 1. Import raw dataset, converting timestamp to datetime
df = pd.read_csv("Insurance_claims_event_log.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 2. Define and form table for the date of First Notification of Loss (FNOL)
fnol_df = df[df["activity_name"] == "First Notification of Loss (FNOL)"][
    ["case_id", "timestamp"]
].rename(columns={"timestamp": "fnol_date"})

# 3. Define and form table for the date of Payment Sent
pay_df = df[df["activity_name"] == "Payment Sent"][
    ["case_id", "timestamp", "claim_amount"]
].rename(columns={"timestamp": "pay_date"})

# 4. Merge FNOL and Payment sent dates using case id
merged_df = pd.merge(fnol_df, pay_df, on="case_id")

# 5. Calculate the development days by subtracting FNOL date from Payment sent date
merged_df["dev_days"] = (
    merged_df["pay_date"] - merged_df["fnol_date"]
).dt.days

# 6. Convert the date into month
merged_df["fnol_month"] = merged_df["fnol_date"].dt.to_period("M")
merged_df["pay_month"] = merged_df["pay_date"].dt.to_period("M")

# 7. Calculate the development months
merged_df["dev_month"] = (
    merged_df["pay_month"].dt.year - merged_df["fnol_month"].dt.year
) * 12 + (merged_df["pay_month"].dt.month - merged_df["fnol_month"].dt.month)

# 8. Print out the details to check the aggregations
print(
    merged_df[
        [
            "case_id",
            "fnol_date",
            "pay_date",
            "dev_days",
            "fnol_month",
            "dev_month",
        ]
    ].to_string()
)




print(f"Total claims processed: {len(merged_df)}")

# 9. Construct the incremental loss triangle
incremental_triangle = merged_df.pivot_table(
    index="fnol_month",
    columns="dev_month",
    values="claim_amount",
    aggfunc="sum",
)

# 10. Construct the cumulative triangle
cumulative_triangle = incremental_triangle.cumsum(axis=1)

# 11. Generate the cumulative triangle
print("\n=== Monthly Cumulative Loss Triangle ($) ===")
print(cumulative_triangle)

# 12. Export the cumulative triangle
cumulative_triangle.to_excel('Loss_Reserve_Table.xlsx', index=True)
