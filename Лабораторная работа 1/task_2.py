# TODO Найдите количество книг, которое можно разместить на дискете

num_pages = 100
num_lines_per_page = 50
num_chars_per_line = 25
bytes_per_char = 4

disk_size_mb = 1.44
disk_size_bytes = disk_size_mb * 1024 * 1024

book_size_chars = num_pages * num_lines_per_page * num_chars_per_line
book_size_bytes = book_size_chars * bytes_per_char

num_books = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(num_books))

