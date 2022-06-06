#One member tuple
print('#Tuple with one member')
one_member_tuple = ('Only Member',)
print(one_member_tuple)
print('\n')

#ip address tuple
print('#Two member IP address tuple')
ip_addr = ('192.168.0.2', 8080)
print(ip_addr[1])
print('\n')

#Nested tuple
nst_tuple = ('545454', ('Sande','Sydney', 24), 'Kitale')
print('Address: ' + nst_tuple[0])
print('Surname: ' + nst_tuple[1][0])
print('Lastname: ' + nst_tuple[1][1])
print('Age: ' + str(nst_tuple[1][2]))
print('City: ' + nst_tuple[2])
print('\n')