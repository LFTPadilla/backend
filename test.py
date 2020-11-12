#content of test_sample.py
#Solo hay que correr la instruccion 'pytest' desde la consola. Nada +

def inc(x):
	return x+1;

def test_answer():
	assert inc(4) == 5;
