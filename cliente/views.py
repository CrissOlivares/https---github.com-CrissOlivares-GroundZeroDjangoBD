from django.shortcuts import render, get_object_or_404,redirect
from .forms import PaymentInfoForm,RegisterForm
from .models import PaymentInfo  # Importa el modelo PaymentInfo
# Create your views here.
TEMPLATE_DIRS=(
    'os.path.join(BASE_DIR, "templates"),'
)
def GroundZeroInicio(request):
    return render(request,'GroundZeroInicio.html')

def GorundZeroCompra(request):
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('GorundZeroCompra.html')  # Redirige a la página de éxito después de guardar el formulario
    else:
        form = PaymentInfoForm()
    
    return render(request, 'GorundZeroCompra.html', {'form': form})

def GroundZeroArtistas(request):
    return render(request,'GroundZeroArtistas.html')

def GroundZeroCuadros(request):
    return render(request,'GroundZeroCuadros.html')

def GroundZeroEsculturas(request):
    return render (request,'GroundZeroEsculturas.html')

def GroundZeroOrfebreria(request):
    return render (request,'GroundZeroOrfebreria.html')

def GroundZeroLogin(request):
    return render (request,'GroundZeroLogin.html')

def GroundZeroRegister(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('GroundZeroLogin.html')  # Redirigir a una página de éxito o inicio de sesión
    else:
        form = RegisterForm()
    
    return render(request, 'GroundZeroRegister.html', {'form': form})

def GroundZeroPaises(request):
    return render(request,"GroundZeroPaises.html")

def GroundZeropPQ(request):
    return render(request,'GroundZeropPQ.html')

def index(request):
    return render(request,'index.html')

def login_view(request):
    return render(request, 'registration/login.html')

def lista_tarjetas(request):
    tarjetas = PaymentInfo.objects.all()  # Obtiene todas las instancias de PaymentInfo desde la base de datos
    context = {'tarjetas': tarjetas}  # Crea el contexto con las tarjetas obtenidas
    return render(request, 'lista_tarjetas.html', context)

def editar_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(PaymentInfo, id=tarjeta_id)
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST, instance=tarjeta)
        if form.is_valid():
            form.save()
            return redirect('lista_tarjetas.html')  # Redirige a la lista de tarjetas después de editar
    else:
        form = PaymentInfoForm(instance=tarjeta)
    
    return render(request, 'editar_tarjeta.html', {'form': form})

def eliminar_tarjeta(request, tarjeta_id):
    tarjeta = get_object_or_404(PaymentInfo, id=tarjeta_id)
    if request.method == 'POST':
        tarjeta.delete()
        return redirect('lista_tarjetas.html')  # Redirige a la lista de tarjetas después de eliminar
    else:
        return render(request, 'eliminar_tarjeta.html', {'tarjeta': tarjeta})
    
def success(request):
    return render(request, 'success.html')

def menu(request):
    request.session["usuario"]="miguel"
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render (request,'./registration/GroundZeroLogin.html')