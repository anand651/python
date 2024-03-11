'''******************** we can import os because it work is to clear the screen ********************'''
import os
print("******************** welcome to the silent auction program ******************")
def find_winner(bidder_details):
    highest_bid=0
    winner = ""
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"here is the list of all the bidders:{bidder_details}")
    print(f"the winner is {winner} with a bid price of {highest_bid}")


bidder_data={}
end_of_bidding=False
while not end_of_bidding:
         name=input("what is your name ?: ")
         price=int(input("what is your bid ?: "))
         bidder_data[name]=price
         more_bidders=input("are there more bidders ? type 'yes' or 'no' : " ).lower()
         if more_bidders=='no':
             end_of_bidding=True
             find_winner(bidder_data)
         elif more_bidders=='yes':
             os.system('cls')



'''what is your name ?: anand
what is your bid ?: 100
are there more bidders ? type 'yes' or 'no' : yes'''

'''what is your name ?: raja
what is your bid ?: 200
are there more bidders ? type 'yes' or 'no' : no
here is the list of all the bidders:{'anand': 100, 'raja': 200}
the winner is raja with a bid price of 200

Process finished with exit code 0

'''



'''what is your name ?: anand
what is your bid ?: 100
are there more bidders ? type 'yes' or 'no' : yes
what is your name ?: raja
what is your bid ?: 200
are there more bidders ? type 'yes' or 'no' : yes
what is your name ?: dezy
what is your bid ?: 300
are there more bidders ? type 'yes' or 'no' : no
the winner is dezy with a bid price of 300'''