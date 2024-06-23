'''Python program on Chemist Shop Made By Anuraj And Arjun
Class 12th B'''
import csv
print('------------Chemist Shop-------------')
print('')
pname=input("Please enter your name:")
pname1=pname.capitalize()
f=open("userdata.txt","r")
q1=f.read()
if pname1 in q1:
	print(f'Welcome back @{pname1}')
	date1=input('hey '+pname1+',Please enter todays date:')
else:
	f=open("userdata.txt","a+")
	print(pname1+" Welcome to our store! ")
	date1=input('hey '+pname1+',Please enter todays date:')
	urecord=("name :"+pname1, "Date used:"+date1)
	f.write(str(pname)+'\n')
	f.close

while True:
	def menu():
		print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
		print("   ")
		print("______________________________   ")
		print("Add a NEW PRODUCT by pressing '1' ")
		print('______________________________')
		print("CHECK STOCK by pressing'2' ")
		print('______________________________')
		print("DELETE A PRODUCT by pressing '3' ")
		print('______________________________')
		print("Genrate a NEW BILL by pressing '4' ")
		print("_____________________________")
		print("Open CUSTOMER DATABASE by pressing '5' ")
		print("_____________________________")
		print("Check LOGIN HISTORY by pressing '10' ")
		print("_________________________________")
		print("MODIFY FILE CONTENTS by pressing '11'")
		print('_______________________________')
		print("OPEN SYSTEM SETTING by pressing 100")
		print('')
		print("know ABOUT US by pressing '7'")
		print('______________________________')
		print('')
		print("")
		print("Press 0 to EXIT!")
		print('')
		print('')

	def write_csv():
		 f=open("sample_2.csv","a+",newline='')
		 wo=csv.writer(f)
		 while True:
			 D_id=int(input("Enter Id:"))
			 name=input("Enter Name:")
			 brand=input("Enter brand:")
			 gst=int(input("Enter gst:"))
			 price=int(input("Enter Price of product:"))
			 stock=int(input("Enter Stock:"))
			 data=[D_id,name,brand,gst,price,stock]
			 wo.writerow(data)
			 ch=input("Do you want to enter more records(Y/N):")
			 if ch in 'Nn':
		 		f.close()
		 		break

			
	menu()
	try:
		choice=int(input('Enter your choice:'))
	except:
		print("Try again")
		choice=int(input('Enter your choice:'))
	n = 1
	med = dict()
	while n >= 1:
			    break
			    print(" ")
			    try:
			    	choice = int(input('Enter your choice: '))
			    except:
			    	print('Input was not correct! \n Try again-\n')
			    	choice = int(input('Enter your choice:'))
			   
			
				
	if choice == 1:
				try:
					write_csv()
				except:
					print("something went wrong")
				
		
	elif choice == 2:
				 f=open("sample_2.csv","r")
				 ro=csv.reader(f)
				 for i in ro:
				 	
				 	print(f"Id ={i[0]} Name={i[1]}  Brand={i[2]} GST={i[3]} price={i[4]} Stock={i[5]} \n")
				 	if int(i[5])<5:
				 		print(f"-Low stock of {i[1]}!- \n")
				 		
				 f.close()
				 input("Press enter to continue")

	elif choice == 3:
		        value_to_delete= input("Please enter name of medicine you want to delete:")
		        csv_file=open("sample_2.csv","r+")
		        csv_reader = csv.reader(csv_file)
		        rows =[]
		        for row in csv_reader:
		        	 if value_to_delete not in row:
		        	 	rows.append(row)
		        	 	
		        csv_file.close()
		        csv_file=open("sample_2.csv","w")
		        csv_writer = csv.writer(csv_file)
		        for row in rows:
		        	csv_writer.writerow(row)
		        csv_file.close()
		        print("Product succesfully deleted from database if exists!")
		        input("Press enter to continue")

		        
		       
	elif choice ==11:
		        u1=input("please enter name of medicine:")
		        csv_file=open("sample_2.csv","r+")
		        csv_reader= csv.reader(csv_file)
		        
		        L=[]
		        for row in csv_reader:
		        		if row[1]==u1:
		        			print(f"\n \n  id={row[0]} name={row[1]} brand={row[2]} gst={row[3]}  price={row[4]} stock={row[5]} \n \n")
		        			print("PRESS \n 1-ID \n 2-NAME \n 3-BRAND \n 4-GST \n 5-PRICE \n 6-STOCK")
		        			p1=int(input("Enter your choice:"))
		        			if p1==1:
		        				id1=int(input("New id:"))
		        				L1=[id1,row[1],row[2],row[3],row[4],row[5]]
		        				L.append(L1)
		        			if p1==2:
		        				name1=input("New name:")
		        				L1=[row[0],name1,row[2],row[3],row[4],row[5]]
		        				L.append(L1)
		        			if p1==3:
		        				brand1=input("New brand:")
		        				L1=[row[0],row[1],brand1,row[3],row[4],row[5]]
		        				L.append(L1)
		        			if p1==4:
		        				gst1=int(input("new gst:"))
		        				L1=[row[0],row[1],row[2],gst1,row[4],row[5]]
		        				L.append(L1)
		        			if p1==5:
		        				price1=int(input("New price:"))
		        				L1=[row[0],row[1],row[2],row[3],price1,row[5]]
		        				L.append(L1)
		        			if p1==6:
		        				stock1=int(input("New stock:"))
		        				L1=[row[0],row[1],row[2],row[3],row[4],stock1]
		        				L.append(L1)

		        		elif row[1] !=u1:
		        			L2=[row[0],row[1],row[2],row[3],row[4],row[5]]
		        			L.append(L2)
		        		continue
		        csv_file.close()
		        csv2=open("sample_2.csv","w+")
		        csww=csv.writer(csv2)
		        for i in L:
		        			csww.writerow(i)
		        csv2.close()

		        	

		        
		        
	elif choice == 10:

			        
			        f=open('userdata.txt','r')
			        m=f.read()
			        print(m)
			        input("\n Press any key to continue.")
			        f.close
				
			    
		        
	elif choice == 100:
			gst=int("25")
			print(f" DAFAULT GST Value: {gst}%")
			print("Files used: \n USER DATA--userdata.txt \n CUSTOMER DATA--customerdata.txt \n STOCK--sample_2.csv ")
			print("For more info reach out to use at chemistShop@gmail.com")
			input("Press any key to continue.")
				
				
	elif choice == 4:
			cname=input("Please enter customer name: ")
			cpno=input("Please enter customer phone number:")
			name2=cname.capitalize()
			try:
				f=open("customerdata.txt","r")
				r=f.read()
				if name2 in r:
					print('Customer found in data base!')
				else:
					print('New Customer!')
					f.close
			except:
				print('file does not exist!')

			f=open("sample_2.csv","r+")
			ro=csv.reader(f)
			wo=csv.writer(f)
			mname=input("Enter the name of medicine:")
			
			for i in ro:
				 if mname==i[1]:
					 id=i[0]
					 name=i[1]
					 print(name)
					 brand=i[2]
					 gst=i[3]
					 price=i[4]
					 Stock=i[5]
					 print(f"---id={id}  name={name}  brand={brand}  GST={gst}  Price={price}  Stock={Stock}---")
					 break
			f.close()
			
				
			print("  ")
			try:
				if name==mname:
					print("Confirming stock!")
					print("Product found in stock!")
			
					
				else:
					print("Product not in stock!")
					price=int(input("Please enter price manually:"))
					gst= int(input("Please enter gst manually"))
			except:
				print("Please make sure stock is Updated")
				continue
				
			try:
				
			
				amount=int(input("Please enter no. units purchased:"))
			except:
				amount=int(input("Please enter no. units purchased:"))
				print("please enter a vaild input")
				
			if int(Stock)<amount:
				print("--Stock is not enough OR product not registered")
				input("press enter to continue.")
			price= int(price)
			price1=(price*amount)
			print(f'total price={price1}')
			price1=int(price1)
			
			f=open("sample_2.csv","r+")
			value_to_delete= mname
			csv_file=open("sample_2.csv","r+")
			csv_reader = csv.reader(csv_file)
			rows =[]
			for row in csv_reader:
			       	 		
			       	 		if value_to_delete not in row:
			       	 			rows.append(row)
			       	 		if value_to_delete in row:
			       	 			Stock1=int(Stock)-amount
			       	 			if Stock1<0:
			       	 				Stock1=int(0)
			       	 			L1=[id,name,brand,gst,price,Stock1]
			       	 			rows.append(L1)
			       	 		f.close
			csv_file.close()
			csv_file=open("sample_2.csv","w")
			csv_writer = csv.writer(csv_file)
			for i in rows:
			       csv_writer.writerow(i)
			csv_file.close()

			f.close
			f.close
				
			
			print("\n")
			i1=1
			if i1==1:
				price2=(int(gst)/100)*price1
				price2=price1+price2
				print(f"Total price after gst({gst}) is {price2}")
				print(f"stock:{Stock}")
					
			else:
				price2=(gst/100)*price1
				price2=price1+price2
				print(f"Total price after gst({gst}) is-{price2}")
					
			
			f.close
			pay=int(input("Card Or Cash? \n Press 0 for card :"))
			if pay<1:
				print(f"Please swipe you card in card machine to pay ₹{price2}")
			else:
				print(f"Please pay ₹{price2} in cash.")
				
			print("")
			print("--------------------Bill-----------------")
			
			print(f'your Name:{cname}')
			print(f'Product purchased:{name}')
			print(f'Your Phone.No:{cpno}')
			print(f'Date of purchase:{date1}')
			print(f'Total price:{price2}')
			print(f'GST:{gst}')
			if (name2 != pname1):
				print('')
				print('Thanks for visiting!')
			else:
				print('have a nice day!')
			print("\n No singnature required")
			price1=str(price1)
			
			record1 = ("CN = "+name2, "  PN = "+cpno, "  DOP = "+date1, "  Pd.P ="+mname, "  TP ="+price1  ,"\n")
			record = str()
			f=open('customerdata.txt','a+')
			f.writelines(record1)
			f.close
			
			input("\n \n Press any key to continue")
				
			
			
			
			
	elif choice ==5 :
				try:
					f=open('customerdata.txt','r+')
					i=f.read()
					print(" CN=CUSTOMER NAME \n PN=PHONE NUMBER \n DOP= DATE OF PURCHASE \n TP= TOTAL PRICE \n Pd.P= PRODUCT PURCHASED \n \n")
					
					print(i)

					f.close
				except:
					print('file does not exist!')
				input("Press any key to continue.")
				
	elif choice == 7:
			print('')
			print('')
			print('------Anuraj And Arjun Chemist Shop------')
			print('~')
			print('This program was made by two students Anuraj and Arjun during there summer vacation in year 2022 . \n They are currently studying in Air Force Golden Jubilee Institute and planning to extend there buisness  ')
			print('')
			print('*We are not non profit oragnisation*')
			print('If you want to support us please click on link given below')
			print('')
			print(' https://docs.google.com/document/d/1fkGrFkzFKxTq7P6hSrgYJIR-FuZJjqwewHVeTbjnddM/edit?usp=drivesdk ')
			input("Press any key to continue.")
			
	if choice == 0:
		     	   print('')
		     	   print('*Closing program*')
		     	   print(f'Thanks for using our software :) @{pname1}!')
		     	   break
		     	   
	else:
		 print("Please make sure your input is valid! \n Try again")
		 continue
		 
		 
