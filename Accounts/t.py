"""import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid ='ACe20147b02a1c22b113a77e8fe0726b27'
auth_token = '7e5ea1cea97eaedc5d41351c2e56eff4'
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="please join to the meetings link: https://htmlcoders.com",
                     from_='+12565308206',
                     to='+916304829813'
                 )

print(message.sid)


message = client.messages \
    .create(
         from_='whatsapp:+12565308206',
         body='Hi, Joe! Thanks for placing an order with us. We’ll let you know once your order has been processed and delivered. Your order number is O12235234. Thanks',
         to='whatsapp:+916304829813'
     )

print(message.sid)


l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

# sorted list
print("Sorted List", l1)
"""

t=["aa","ac","ab","ade","afg",]


l1=[]
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i]>=t[j]:
            print(i,j)
            print(t[i]>=t[j])
            t[i],t[j]=t[j],t[i]
        else:
            print(i, j,"ok")

print(t)



"""
k=sorted(t)
j = ""
p=()
l=[]
for i in range(0,len(k),2):
    if i+1<len(k):
        p=(k[i],k[i+1])

        l.append(p)

    else:
        l.append((k[i]))
print(l)"""
