def find_missing(a_list, b_list):

    odd_one_out = 0

    for b_element in b_list:
        if b_element not in a_list:
            odd_one_out = b_element

    return odd_one_out
