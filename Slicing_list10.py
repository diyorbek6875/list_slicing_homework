def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    s=list1[n:]
    return s[::-1]
n=int(input())
print(main([1,2,3,4,5,6,7,9],n))