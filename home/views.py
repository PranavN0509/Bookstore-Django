from django.shortcuts import render
from django.db.models import Q
from Books.models import *
from order.models import Order, OrderItem

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        context = {'Books' : Book.objects.all().order_by('-created_at')[:4]}
        return render(request, "home/index.html", context)
        # latest_ordered_books = []
        # previous_orders = Order.objects.filter(customer = request.user).order_by('-created_at')[:2]
        # print(previous_orders)
        # for order in previous_orders:
        #     order_items = OrderItem.objects.filter(order = order)
        #     print(order_items.count())
        #     if(order_items.count()>=2):
        #         for items in order_items:
        #             latest_ordered_books.append(items.book)
        #             if len(latest_ordered_books)>=2:
        #                 break
        #     elif(order_items.count()>=1):
        #         for items in order_items:
        #             if len(latest_ordered_books)>=2:
        #                 break
        #             latest_ordered_books.append(items.book) 
        #         continue
        # print("Latest ordered books list: ",latest_ordered_books)
    


def allbooks(request):
    context = {'Books' : Book.objects.all().order_by('name'), 'categories': Category.objects.all()}
    return render(request, "home/allbooks.html", context)



def get_book_category(request, cat_id):
    context = {'Books': Book.objects.filter(category_id=cat_id), 'categories': Category.objects.all()}
    return render(request, "home/allbooks.html", context)



def book_search(request):
    print(request)
    search = request.GET.get('search_query')
    if search=="":
        context = {'Books' : Book.objects.all().order_by('-created_at')[:4]}
        return render(request, "home/index.html", context)
        
    
    print("Hello inside search")
    books = Book.objects.all()
    if search:
        books = books.filter(
            Q(name__icontains=search)|Q(category__name__icontains=search)|Q(writer__name__icontains=search)
        )
    print(books)
    context = {
        "Books": books,
        "search": search,
        "categories": Category.objects.all()
    }
    return render(request, 'home/index.html', context)