import time

from testMain import Instagram_Web_Scrapping_Followers_Count

main = Instagram_Web_Scrapping_Followers_Count.Surya


def test_1():
    method_of_login = input("Choose the method of login: Instagram or Facebook: ")
    # Choose the method of login:
    if method_of_login == "Instagram" or "instagram" or "insta":
        main.insta_login_with_credentials()
    elif method_of_login == "Facebook" or "facebook" or "fb":
        main.insta_login_using_fb()
    else:
        print("Provide proper method of login")
        return test_1()


def test_2():
    # Search the user
    time.sleep(2)
    main.Search_user()


def test_3():
    # get the details of the user
    main.get_details()
