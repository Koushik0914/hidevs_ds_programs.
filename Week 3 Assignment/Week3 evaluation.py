# lst = [ 1,2,121,2,12,121,2142131,121,2121,2121]
# this is list and you have filter even and odd numbers from above list and save into a dict like this: {'even': [], 'odd': [], 'prime': [], 'total_values': [], 'duplicate':[], 'frequency_no': {'1':2, '2': 4}}
# Deepak Chawla20:54
# - User input will be taken.
# - Proper error handling will be ensured using try and except with proper message on errors.
# - Code will be converted into a function.
# - Optimizations will be applied like try to remove for loop or if else or unwanted append code
# - Validations will be implemented.
# - Incorrect input will be retried three times. After three attempts, the user will exit the function.

list = (input("Enter a list with comma separated: ").split(","))

counter=0
def check_list(lst,counter):
    even=[]
    odd=[]
    prime=[]
    total_values=[]
    duplicate=[]
    frequency_no={}

    try:
        for i in lst:
            frequency_no[i]=1
            if int(i)%2==0:
                even.append(i)
            else:
                odd.append(i)
            if i in total_values:
                frequency_no[i] = int(frequency_no[i])+1
                duplicate.append(i)
            else:
                total_values.append(i)
            is_prime=1
            for j in range(2,int(i)+1):
                if j%int(i)==0:
                    is_prime=0
            if is_prime:
                prime.append(i)
        dict = {'even': even, 'odd': odd, 'prime': prime, 'total_values': total_values, 'duplicate': duplicate,
                'frequency_no': frequency_no}
        print(dict)

    except ValueError:
        counter = counter + 1
        if counter > 2:
            print('limit exceeded')
        else:
            print('Try again and Enter only integers')
            list = (input("Enter a list with comma separated: ").split(","))
            check_list(list,counter)



check_list(list,counter)
