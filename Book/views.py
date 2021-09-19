from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Book
from django.shortcuts import redirect
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


# Create your views here.



# def func(request):
#     return render(request, "home.html")
    # return HttpResponse("Hi hello guys")

def email_func(body):
    " To send email "
    mail = EmailMessage(subject="Django Book details", body=body, from_email = settings.EMAIL_HOST_USER, to=["bhombeashish@gmail.com"])
    mail.send(fail_silently=False)

def homepage(request):
    " Go to Homepage of book Library        "
    if request.method == "POST":
        data = request.POST
        if not data.get("id"):
            if data["Is_pub"] == "Yes":
                Book.objects.create(name = data["nm"], 
                qty = request.POST["qty"],
                price = data["price"],
                is_published = True,
                published_date = date.today())
            elif data["Is_pub"] == "No":
                Book.objects.create(name = data["nm"], 
                qty = data["qty"],
                price = data["price"],
                is_published = False)
            email_func(body=f"Your Book '{data['nm']}' successfully created")
            return redirect("home")
        else:
            bid = data.get("id")    
            book_obj = Book.objects.get(id = bid)
            book_obj.name = data["nm"]
            book_obj.qty = data["qty"]
            book_obj.price = data["price"]
            if data["Is_pub"] == "Yes":
                if book_obj.is_published:
                    pass
                else:
                    book_obj.is_published = True
                    book_obj.published_date = date.today()

            elif data["Is_pub"] == "No":
                if book_obj.is_published == True:
                    pass
            book_obj.save()
            return redirect("home")
    else:
        return render(request, template_name= "home.html")

def get_book(request):
    " To get book as per request "
    book = Book.objects.all()
    return render(request, template_name = "book.html", context= {"all_books": book})

def hard_delete(request, id):
    " To delete book permenently "
    book = Book.objects.get(id = id )
    email_func(body=f"Your Book '{book.name}' permanently deleted successfully...!")
    book.delete()
    return redirect("showbook")

def Update_book(request, id):
    " To update the book detials"
    book = Book.objects.get(id = id)
    email_func(body=f"Your Book '{book.name}' Updated successfully...!")
    return render(request, "home.html", context= {"Update_Book": book })

def soft_delete(request, id):
    " To soft delete book details "
    book = Book.objects.get(id = id)
    book.is_deleted = 0
    book.save()
    email_func(body=f"Your Book '{book.name}' soft deleted successfully...!")
    return redirect("showbook")

def restore(request, id):
    "To restore the book detials"
    book = Book.objects.get(id = id)
    book.is_deleted = 1
    book.save()
    email_func(body= f"Your Book '{book.name}' restore successfully...!")
    return redirect("showbook")

def active_book(request):
    " To show active book "
    active_books = Book.objects.filter(is_deleted = 1)
    return render(request, "book.html", context={"all_books": active_books})

def in_active_book(request):
    "to show inactive book "
    in_active_books = Book.objects.filter(is_deleted = 0)
    return render(request, "book.html", context={"all_books": in_active_books, "data_type": "InActive"})
