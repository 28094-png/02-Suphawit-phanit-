# ==========================================
# โจทย์ข้อที่ 4: สัญญาณไฟจราจร
# Input: สีของสัญญาณไฟ ("red", "yellow", "green")
# Output: พิมพ์ "Stop" ถ้าเป็น red | "Slow" ถ้าเป็น yellow | "Go" ถ้าเป็น green | "Invalid" กรณีอื่นๆ
# ==========================================


# นักเรียนเขียนโค้ดต่อจากบรรทัดนี้
color = input()
if (color == ("Stop")):
    print("red")
elif (color == ("Slow")):
    print ("yellow")
elif (color == ("Go")):
    print ("green")
else:
    print ("Invalid")
