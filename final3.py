
class Library():
    def __init__(self,list,name):
        self.booklist=list
        self.libraryname=name
        self.lenddict={}

    def displaybook(self):
        for book in self.booklist:
            print(book)

    def lendbook(self,book,user):
        from datetime import datetime
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print(f"Book have been issued to {user} on {datetime.now()}  ")
        else:
            print(f"book is been already issued to {self.lenddict[book]}")

    def addbook(self):
        self.booklist.append()

    def returnbook(self,book):
        self.lenddict.pop(book)

if __name__ == '__main__':

   guddu=Library({'python','rich dad poor dad','7 habits','revolution 2020','she friendzoned my love','it started with a friend request','ignited mind'},'THE GUDDU')
   while(True):
          print(f"welcome to {guddu.libraryname} library.Enter your choice")
          print("1-Display list of books")
          print("2-Lend a book")
          print("3-Add a book")
          print('4-Return a book')
          user_choice=input()
          if user_choice  not in ['1','2','3','4']:
             print('Please enter a vaid input')
             continue
          else:

               if user_choice=='1':
                   print('We have following books in our Library')
                   guddu.displaybook()

               elif user_choice=='2':
                  book=input("Enter the name of book you want to lend:")
                  if book in guddu.booklist:
                         user=input("Enter you name:")
                         guddu.lendbook(book,user)
                  else:
                       print('Sorry!!! No result found')

               elif user_choice=='3':
                   guddu.addbook()
                   print('Book is added to Library')
               elif user_choice=='4':
                   book=input('Enter the name of book you want to return')
                   guddu.returnbook(book)
          print('Press q to quit or c to continue')
          user_choice2 = input(" ")
          while(user_choice2!='c' and user_choice2!='q'):


              if user_choice2=='q':
                  exit()
              elif user_choice2=='c':
                  continue

















