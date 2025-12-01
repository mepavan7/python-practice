def print_rangoli(size):
    import string
    all_letters = string.ascii_lowercase
    first_letters = all_letters[0:size]
    reverse_first_letters = first_letters[::-1]
    top_lines = []
    total_width = (4 * size) - 3
    for i in range(size):
        left_part = reverse_first_letters[0:i+1]
        right_part = left_part[:-1][::-1]
        full_part = [*left_part, *right_part]
        res = "-".join(full_part)
        centered_lines = res.center(total_width, "-")
        top_lines.append(centered_lines)
    bottom_lines = top_lines[:-1][::-1]
    final_list = top_lines + bottom_lines
    final_list = '\n'.join(final_list)
    print(final_list)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
        
    