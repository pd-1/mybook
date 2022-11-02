from django.shortcuts import render, get_object_or_404 ,redirect
from django.http import HttpResponse

from cms.models import Book
from cms.forms import BookForm


def book_list(request):
    books = Book.objects.all().order_by('id')
    return render(request,
                  'cms/book_list.html',     # 使用するテンプレート
                  {'books': books})         # テンプレートに渡すデータ


def book_edit(request, book_id=None):
    if book_id:
        book = get_object_or_404(Book, pk=book_id)
    else:
        book = Book()
        
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('cms:book_list')
    else:
        form = BookForm(instance=book)
        
    return render(request, 'cms/book_edit.html', dict(form=form,book_id=book_id))


def book_del(request,book_id):
    return HttpResponse('書籍の削除')
