# !/usr/bin/env python3
# echo acos acosh asin asinh atan atanh cbrt cos cospi cosh erf erfc exp exp10 exp2 expm1 j0 j1 log log10 log1p log2 rsqrt sin sinpi sinh tan tanpi tanh y0 y1 lgamma tgamma | sed 's/ /\" \"/g'
if __name__ == '__main__':
#	functions = ["acos","acosh","asin","asinh","atan","atanh","cbrt","cos","cospi","cosh","erf","erfc","exp","exp10","exp2","expm1","j0","j1","log","log10","log1p","log2","rsqrt","sin","sinpi","sinh","tan","tanpi","tanh","y0","y1","lgamma","tgamma"]
	functions = ["acos","acosh","asin","asinh","atan","atanh","cbrt","cos","cosh","erf","erfc","exp","exp10","exp2","expm1","j0","j1","log","log10","log1p","log2","sin","sinh","tan","tanh","y0","y1","lgamma","tgamma"]
	print("// auto generated")
	print("#include<cmath>")
	print("")
	print("int main() {")
	print("")
	print("  int ret = 0;")
	print("  for (int i =-33; i<33; ++i) {")
	for fun in functions:
		print("    ret += "+fun+"f(float(i));")
		print("    ret += "+fun+"(double(i));")
	print("  }")
	print("")
	print("double x = std::pow(2,-129);");
	print("  for (int i =0; i<258; ++i) {")
	print("    x*=2;")
	for fun in functions:
		print("    ret += "+fun+"f(float(x));")
		print("    ret += "+fun+"(double(x));")
	print("  }")
	print("  return ret;");
	print("}")
