from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>HOME PAGE<h1> <br>'
                        '<a href="http://127.0.0.1:8000/one/"><button>next</button></a>')


def one(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №1!<h1> <br>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>next</button></a>')


def two(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №2!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/one/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>next</button></a>')


def three(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №3!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/two/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>next</button></a>')


def four(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №4!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/three/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>next</button></a>')


def five(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №5!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/four/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>next</button></a>')


def six(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №6!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/five/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>next</button></a>')


def seven(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №7!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/six/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>next</button></a>')


def eight(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №8!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>next</button></a>')


def nine(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>10</button></a>  <hr><br>'
                        '<h1>Bu sahifa №9!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>'
                        '<a href="http://127.0.0.1:8000/ten/"><button>next</button></a>')


def ten(request):
    return HttpResponse('<a href="http://127.0.0.1:8000/one/"><button>1</button></a>'
                        '<a href="http://127.0.0.1:8000/two/"><button>2</button></a>'
                        '<a href="http://127.0.0.1:8000/three/"><button>3</button></a>'
                        '<a href="http://127.0.0.1:8000/four/"><button>4</button></a>'
                        '<a href="http://127.0.0.1:8000/five/"><button>5</button></a>'
                        '<a href="http://127.0.0.1:8000/six/"><button>6</button></a>'
                        '<a href="http://127.0.0.1:8000/seven/"><button>7</button></a>'
                        '<a href="http://127.0.0.1:8000/eight/"><button>8</button></a>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>9</button></a>  <hr><br>'
                        '<h1>Bu sahifa №10!<h1> <br>'
                        '<a href="http://127.0.0.1:8000/nine/"><button>prev</button></a>'
                        '<a href="http://127.0.0.1:8000"><button>Home</button></a>')