try:
    with(
       open ("file1.txt") as f1,
       open ("file2.txt") as f2,
       open ("file3.txt") as f3
    ):
        content1 = f1.read
        print(content1)
        content2 = f2.read
        print(content2)
        content3 = f3.read
        print(content3)

except FileNotFoundError as e:
    print(f"Error: {e} in file number {e.filename}")

finally:
    print("Code executed successfully...")