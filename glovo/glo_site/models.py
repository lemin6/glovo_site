from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    age = models.PositiveIntegerField(default=0)
    date_registered = models.DateField(auto_now=True)
    email = models.EmailField()
    phone_number = models.IntegerField()
    STATUS_CHOICES = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
        ('simple', 'Simple'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.first_name


class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Food(models.Model):
    resto_name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gramm = models.DecimalField(max_digits=10, decimal_places=2)


class Courier(models.Model):
    courier_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    STATUS_CHOICES = (
        ('пешком', 'Пешком'),
        ('велосипед', 'Велосипед'),
        ('мотоцикл', 'Мотоцикл'),
        ('авто', 'Авто'),
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return self.courier_name


class Order(models.Model):
    order_number = models.CharField(max_length=100)
    recipient_name = models.CharField(max_length=100)
    recipient_phone = models.CharField(max_length=20)
    delivery_address = models.TextField()
    delivery_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_number


class Delivery(models.Model):
    order_number = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('в обработке', 'В обработке'),
        ('в пути', 'В пути'),
        ('доставлен', 'Доставлен'),
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)

    def __str__(self):
        return self.order_number


class Rating(models.Model):
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], help_text="Rate the item with 0 to 6 stars.", verbose_name="Rating")

    def __str__(self):
        return f"{self.product} - {self.user} - {self.stars} stars"


class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    product = models.ForeignKey(Food, related_name='reviews', on_delete=models.CASCADE)
    parent_review = models.ForeignKey('self', related_name='replies', null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)