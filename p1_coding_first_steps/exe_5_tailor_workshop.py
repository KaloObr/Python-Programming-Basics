tables_count = int(input())
table_lenght = float(input())
table_width = float(input())

price_table_cover = 7
price_kare_cover = 9
bgn = 1.85

table_cover_area = tables_count * (table_lenght + 2 * 0.30) * (table_width + 2 * 0.30)
kare_cover_area = tables_count * (table_lenght/2) * (table_lenght/2)

total_price = table_cover_area * price_table_cover + kare_cover_area * price_kare_cover

print(f"{total_price:.2f} USD")
print(f"{total_price * bgn:.2f} BGN")
