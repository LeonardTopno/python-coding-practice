def totalGuests(Pi,N):
    guest_count = 0
  
    for i in range(N):
  	    if Pi[i] <= guest_count:
            guest_count = guest_count+1 
      
    return guest_count
  
#Driver Code
N = 5
Pi = [1,0,2,1,3] # This is a list
  
Num_of_guests = totalGuests(Pi, N)
print("Total Number:", Num_of_guests)