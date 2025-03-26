from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Library
from .forms import LibraryForm # type: ignore
from django.contrib import messages # type: ignore

# Create your views here.
def book_list(request):
    librarys = Library.objects.all()
    return render(request, 'library_app/book_list.html', {'librarys': librarys})

def insert_book(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Library added successfully!')
            return redirect('book-list')
    else:
        form = LibraryForm()
    return render(request, 'library_app/insert_book.html', {'form': form})

def view_book(request, pk):
    library = get_object_or_404(Library, pk=pk)
    return render(request, 'library_app/view_book.html', {'library': library})

def edit_book(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        form = LibraryForm(request.POST, instance=library)
        if form.is_valid():
            form.save()
            messages.success(request, 'Library Details updated successfully!')
            return redirect('book-list')
        else:
            messages.error(request, 'Error updating library. Please check the form.')
    else:
        form = LibraryForm(instance=library)
    
    return render(request, 'library_app/insert_book.html', {'form': form, 'update': True, 'library': library})

def delete_book(request, pk):
    library = get_object_or_404(Library, pk=pk)
    if request.method == 'POST':
        library.delete()
        messages.success(request, 'Library deleted successfully!')
        return redirect('book-list')
    return render(request, 'library_app/delete_book.html', {'library': library})
