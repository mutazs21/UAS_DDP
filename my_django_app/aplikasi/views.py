from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def index(request):
    featured_recipes = [
        {
            'id': 1,
            'title': 'Nasi Goreng Sederhana',
            'description': 'Nasi goreng enak dengan bumbu dapur',
            'budget': 8000,
            'cooking_time': 15,
            'image': 'https://assets.unileversolutions.com/recipes-v2/258055.jpg'  
        },
        {
            'id': 2,
            'title': 'Mie Goreng Telur',
            'description': 'Mie instan digoreng dengan telur',
            'budget': 6000,
            'cooking_time': 10,
            'image': 'https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/08/01045246/ini-resep-mie-goreng-dengan-bahan-sederhana-yang-menggugah-selera-halodoc.jpg.webp'  
        },
        {
            'id': 3,
            'title': 'Capcay Hemat',
            'description': 'Tumis sayuran bergizi',
            'budget': 12000,
            'cooking_time': 20,
            'image': 'https://cdn0-production-images-kly.akamaized.net/CqSVKBFZK5RdW-xDDOi8BTZsGgM=/1200x675/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/3147148/original/023254000_1591628473-051260000_1465292757-royco.coid.jpg' 
        }
    ]
    
    context = {
        'featured_recipes': featured_recipes
    }
    return render(request, 'index.html', context)

def home(request):
    return render(request, 'home.html')

def recipes(request):
    recipes_list = [
        {
            'id': 1,
            'title': 'Nasi Goreng Sederhana',
            'description': 'Nasi goreng enak dengan bumbu dapur sederhana',
            'budget': 8000,
            'cooking_time': 15,
            'servings': 1,
            'image': 'https://assets.unileversolutions.com/recipes-v2/258055.jpg'  
        },
        {
            'id': 2,
            'title': 'Mie Goreng Telur',
            'description': 'Mie instan digoreng dengan telur mata sapi',
            'budget': 6000,
            'cooking_time': 10,
            'servings': 1,
            'image': 'https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/08/01045246/ini-resep-mie-goreng-dengan-bahan-sederhana-yang-menggugah-selera-halodoc.jpg.webp'  
        },
        {
            'id': 3,
            'title': 'Capcay Hemat',
            'description': 'Tumis sayuran bergizi dan lezat',
            'budget': 12000,
            'cooking_time': 20,
            'servings': 2,
            'image': 'https://cdn0-production-images-kly.akamaized.net/CqSVKBFZK5RdW-xDDOi8BTZsGgM=/1200x675/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/3147148/original/023254000_1591628473-051260000_1465292757-royco.coid.jpg'  
        },
        {
            'id': 4,
            'title': 'Telur Dadar Isi',
            'description': 'Telur dadar dengan sayuran',
            'budget': 5000,
            'cooking_time': 8,
            'servings': 1,
            'image': 'https://assets.unileversolutions.com/v1/1786169.jpg'  
        },
        {
            'id': 5,
            'title': 'Tumis Kangkung',
            'description': 'Kangkung tumis terasi pedas',
            'budget': 7000,
            'cooking_time': 12,
            'servings': 2,
            'image': 'https://assets.unileversolutions.com/recipes-v2/230520.jpg'  
        },
        {
            'id': 6,
            'title': 'Soto Ayam Sederhana',
            'description': 'Soto ayam hangat untuk makan siang',
            'budget': 15000,
            'cooking_time': 25,
            'servings': 1,
            'image': 'https://assets.pikiran-rakyat.com/crop/0x0:0x0/720x0/webp/photo/2023/08/18/805485417.jpg'  
        }
    ]
    
    # Filter berdasarkan budget
    budget_filter = request.GET.get('budget', '')
    time_filter = request.GET.get('time', '')
    search_query = request.GET.get('search', '').lower()
    
    filtered_recipes = recipes_list
    
    # Filter budget
    if budget_filter:
        budget_limit = int(budget_filter)
        filtered_recipes = [r for r in filtered_recipes if r['budget'] <= budget_limit]
    
    # Filter waktu
    if time_filter:
        time_limit = int(time_filter)
        filtered_recipes = [r for r in filtered_recipes if r['cooking_time'] <= time_limit]
    
    # Search
    if search_query:
        filtered_recipes = [r for r in filtered_recipes if search_query in r['title'].lower() or search_query in r['description'].lower()]
    
    context = {
        'recipes': filtered_recipes,
        'budget_filter': budget_filter,
        'time_filter': time_filter,
        'search_query': search_query
    }
    return render(request, 'recipes.html', context)

def recipe_detail(request, recipe_id):
    recipes_data = {
        1: {
            'id': 1,
            'title': 'Nasi Goreng Sederhana',
            'description': 'Nasi goreng enak dengan bumbu dapur sederhana yang mudah dibuat',
            'budget': 8000,
            'cooking_time': 15,
            'servings': 1,
            'image': 'https://assets.unileversolutions.com/recipes-v2/258055.jpg', 
            'ingredients_list': [
                '1 piring nasi putih',
                '1 butir telur',
                '2 siung bawang putih',
                '3 siung bawang merah',
                '1 sdm kecap manis',
                '1 sdt garam',
                'Minyak goreng secukupnya'
            ],
            'steps_list': [
                'Iris bawang putih dan bawang merah',
                'Panaskan minyak, tumis bawang hingga harum',
                'Masukkan telur, orak-arik hingga matang',
                'Tambahkan nasi putih, aduk rata',
                'Beri kecap manis dan garam, aduk hingga merata',
                'Masak hingga bumbu meresap, angkat dan sajikan'
            ],
            'tips': 'Gunakan nasi yang sudah dingin agar tidak lembek. Tambahkan daun bawang untuk aroma lebih sedap.'
        },
        2: {
            'id': 2,
            'title': 'Mie Goreng Telur',
            'description': 'Mie instan digoreng dengan telur mata sapi',
            'budget': 6000,
            'cooking_time': 10,
            'servings': 1,
            'image': 'https://d1vbn70lmn1nqe.cloudfront.net/prod/wp-content/uploads/2023/08/01045246/ini-resep-mie-goreng-dengan-bahan-sederhana-yang-menggugah-selera-halodoc.jpg.webp', 
            'ingredients_list': [
                '1 bungkus mie instan',
                '1 butir telur',
                '1 batang daun bawang',
                'Bumbu mie instan',
                'Minyak goreng secukupnya'
            ],
            'steps_list': [
                'Rebus mie hingga setengah matang, tiriskan',
                'Panaskan minyak, goreng telur mata sapi',
                'Sisihkan telur ke pinggir wajan',
                'Tumis mie dengan bumbu instan',
                'Aduk rata hingga bumbu meresap',
                'Sajikan dengan telur di atasnya'
            ],
            'tips': 'Jangan rebus mie terlalu lama agar tidak lembek saat digoreng.'
        },
        3: {
            'id': 3,
            'title': 'Capcay Hemat',
            'description': 'Tumis sayuran bergizi dan lezat',
            'budget': 12000,
            'cooking_time': 20,
            'servings': 2,
            'image': 'https://cdn0-production-images-kly.akamaized.net/CqSVKBFZK5RdW-xDDOi8BTZsGgM=/1200x675/smart/filters:quality(75):strip_icc():format(jpeg)/kly-media-production/medias/3147148/original/023254000_1591628473-051260000_1465292757-royco.coid.jpg', 
            'ingredients_list': [
                '100g kol',
                '100g wortel',
                '50g buncis',
                '2 siung bawang putih',
                '1 sdm saus tiram',
                '1 sdt garam',
                '200ml air',
                '1 sdm maizena'
            ],
            'steps_list': [
                'Potong-potong semua sayuran',
                'Tumis bawang putih hingga harum',
                'Masukkan wortel dan buncis, tumis sebentar',
                'Tambahkan air, masak hingga sayuran setengah matang',
                'Masukkan kol, saus tiram, dan garam',
                'Kentalkan dengan larutan maizena',
                'Masak hingga kuah mengental, angkat'
            ],
            'tips': 'Potong sayuran dengan ukuran sama agar matang merata.'
        },
        4: {
            'id': 4,
            'title': 'Telur Dadar Isi',
            'description': 'Telur dadar dengan isian sayuran sederhana dan bergizi',
            'budget': 5000,
            'cooking_time': 8,
            'servings': 1,
            'image': 'https://assets.unileversolutions.com/v1/1786169.jpg',
            'ingredients_list': [
                '2 butir telur',
                '1 batang daun bawang',
                '1 sdm wortel parut',
                'Garam secukupnya',
                'Merica secukupnya',
                'Minyak goreng secukupnya'
            ],
            'steps_list': [
                'Kocok telur dalam mangkuk',
                'Masukkan daun bawang dan wortel',
                'Tambahkan garam dan merica',
                'Panaskan minyak di wajan',
                'Tuang adonan telur',
                'Masak hingga matang di kedua sisi'
            ],
            'tips': 'Gunakan api kecil agar telur matang merata dan tidak gosong.'
        },
        5: {
            'id': 5,
            'title': 'Tumis Kangkung',
            'description': 'Kangkung tumis terasi pedas khas rumahan',
            'budget': 7000,
            'cooking_time': 12,
            'servings': 2,
            'image': 'https://assets.unileversolutions.com/recipes-v2/230520.jpg',
            'ingredients_list': [
                '1 ikat kangkung',
                '2 siung bawang putih',
                '2 buah cabai merah',
                '1 sdt terasi',
                'Garam secukupnya',
                'Minyak goreng secukupnya'
            ],
            'steps_list': [
                'Petik dan cuci kangkung',
                'Iris bawang putih dan cabai',
                'Panaskan minyak, tumis bumbu hingga harum',
                'Masukkan terasi, aduk rata',
                'Masukkan kangkung',
                'Masak cepat hingga layu, angkat'
            ],
            'tips': 'Masak kangkung sebentar saja biar tetap hijau dan renyah.'
        },
        6: {
            'id': 6,
            'title': 'Soto Ayam Sederhana',
            'description': 'Soto ayam hangat dan gurih untuk makan siang',
            'budget': 15000,
            'cooking_time': 25,
            'servings': 1,
            'image': 'https://assets.pikiran-rakyat.com/crop/0x0:0x0/720x0/webp/photo/2023/08/18/805485417.jpg',
            'ingredients_list': [
                '100g ayam suwir',
                '2 siung bawang putih',
                '2 siung bawang merah',
                '1 batang serai',
                'Garam secukupnya',
                'Kaldu bubuk secukupnya',
                '500ml air'
            ],
            'steps_list': [
                'Tumis bawang putih dan bawang merah',
                'Masukkan serai hingga harum',
                'Tambahkan air dan ayam suwir',
                'Beri garam dan kaldu bubuk',
                'Masak hingga kuah mendidih',
                'Sajikan selagi hangat'
            ],
            'tips': 'Tambahkan jeruk nipis dan sambal biar rasanya naik level.'
        }
    }
    
    # Ambil data resep berdasarkan ID
    recipe = recipes_data.get(recipe_id, recipes_data[1])
    
    context = {
        'recipe': recipe
    }
    return render(request, 'recipe_detail.html', context)

def about(request):
    return render(request, 'about.html')

# ===== FITUR FORM PROCESSING =====

def submit_recipe(request):
    """Form untuk user submit resep mereka sendiri"""
    if request.method == 'POST':
        # Ambil data dari form
        title = request.POST.get('title')
        description = request.POST.get('description')
        budget = request.POST.get('budget')
        cooking_time = request.POST.get('cooking_time')
        ingredients = request.POST.get('ingredients')
        steps = request.POST.get('steps')
        submitter_name = request.POST.get('submitter_name')
        submitter_email = request.POST.get('submitter_email')
        
        # Validasi
        if not all([title, description, budget, cooking_time, ingredients, steps, submitter_name, submitter_email]):
            messages.error(request, 'Semua field harus diisi!')
            return render(request, 'submit_recipe.html')
        
        # Di sini bisa simpan ke database
        # Untuk sekarang kita simpan ke session
        if 'submitted_recipes' not in request.session:
            request.session['submitted_recipes'] = []
        
        submitted_recipe = {
            'title': title,
            'description': description,
            'budget': budget,
            'cooking_time': cooking_time,
            'ingredients': ingredients,
            'steps': steps,
            'submitter_name': submitter_name,
            'submitter_email': submitter_email
        }
        
        request.session['submitted_recipes'].append(submitted_recipe)
        request.session.modified = True
        
        messages.success(request, f'Terima kasih {submitter_name}! Resep "{title}" berhasil dikirim dan akan direview oleh admin.')
        return redirect('submit_recipe')
    
    return render(request, 'submit_recipe.html')

def budget_calculator(request):
    """Kalkulator budget belanja mingguan"""
    result = None
    
    if request.method == 'POST':
        try:
            weekly_budget = float(request.POST.get('weekly_budget', 0))
            meals_per_day = int(request.POST.get('meals_per_day', 3))
            
            # Hitung budget per hari dan per makan
            daily_budget = weekly_budget / 7
            budget_per_meal = daily_budget / meals_per_day
            
            # Saran kategori resep
            if budget_per_meal < 7000:
                category = 'Super Hemat'
                suggestions = ['Telur Dadar Isi', 'Mie Goreng Telur', 'Tumis Kangkung']
            elif budget_per_meal < 10000:
                category = 'Hemat'
                suggestions = ['Nasi Goreng Sederhana', 'Tumis Kangkung', 'Telur Dadar Isi']
            elif budget_per_meal < 15000:
                category = 'Standar'
                suggestions = ['Capcay Hemat', 'Nasi Goreng Sederhana', 'Soto Ayam Sederhana']
            else:
                category = 'Premium'
                suggestions = ['Soto Ayam Sederhana', 'Capcay Hemat', 'Bebek Goreng']
            
            result = {
                'weekly_budget': f'{weekly_budget:,.0f}',
                'daily_budget': f'{daily_budget:,.0f}',
                'budget_per_meal': f'{budget_per_meal:,.0f}',
                'category': category,
                'suggestions': suggestions
            }
            
        except (ValueError, TypeError):
            messages.error(request, 'Mohon masukkan angka yang valid!')
    
    context = {'result': result}
    return render(request, 'budget_calculator.html', context)
