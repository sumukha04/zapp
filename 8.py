class PaliStr:
    def __init__(self):
        self.isPali=False
        def chkpalindrome(self, myStr):
            if myStr==myStr[::-1]:
                self.isPali=True
            else:
                self.isPali=False
                return self.isPali
            
            class PaliInt(PaliStr):
                def __init__(self):
                    self.isPali=False
                    def chkPalindrome(self, val):
                        temp=val
                        rev=0
                        while temp!=0:
                            dig=temp%10
                            rev=(rev*10)+dig
                            temp=temp//10

                            if val==rev:
                                self.iPali=True
                            else:
                                self.isPalil=False
                                return self.isPali
                            st=input("enter a string: ")
                            stObj=PaliStr()
                            if stObj.chkPalindrome(st):
                                print("Given string is a palindrome")
                            else:
                                print("NAH")
                            val=int(input("Enter an integer: "))
                            intObj=PaliInt()
                            if intObj.chkPalindrome(int):
                                print("Palindrome")
                            else:
                                print("NAH")