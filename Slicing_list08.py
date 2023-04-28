def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return list1[::-n]
n=int(input())
print(main(["a",1,'b',3,'c',5,'d',7],n))