from django.contrib.auth import get_user_model
User = get_user_model()
users = []
for i in range(10, 20):
    user = User(first_name='User%dFirstName' % i, last_name='User%dLastName' % i,username='user%d' % i,email='user%d@mydomain.com' % i,password='hashedPasswordStringPastedHereFromStep1!',is_active=True, )
    users.append(user)
 
User.objects.bulk_create(users)
