pip install sympy


import sympy as sp

# Definir as variáveis simbólicas
t, x, y, z, G, c, M = sp.symbols('t x y z G c M')

# Definir as expressões simbólicas para o espaço-tempo e a curvatura
g_tt = -(1 - 2*G*M/(c**2 * sp.sqrt(x**2 + y**2 + z**2 - c**2 * t**2)))
g_xx = 1 / g_tt
g_yy = 1 / g_tt
g_zz = 1 / g_tt
Gamma_ttx = (G*M*x) / (c**2 * (x**2 + y**2 + z**2 - c**2 * t**2)**2)
Gamma_tty = (G*M*y) / (c**2 * (x**2 + y**2 + z**2 - c**2 * t**2)**2)
Gamma_ttz = (G*M*z) / (c**2 * (x**2 + y**2 + z**2 - c**2 * t**2)**2)
Gamma_xxt = Gamma_ttx
Gamma_xxy = -G*M*y / (c**2 * (x**2 + y**2 + z**2 - c**2 * t**2)**2)
Gamma_xxz = -G*M*z / (c**2 * (x**2 + y**2 + z**2 - c**2 * t**2)**2)
Gamma_yyt = Gamma_tty
Gamma_yyx = Gamma_xxy
Gamma_yyz = -G*M*z / (c**2 * (x**2 + y**2 + z**2 - c**2 * t**2)**2)
Gamma_zzt = Gamma_ttz
Gamma_zzx = Gamma_xxz
Gamma_zzy = Gamma_yyz

# Definir a curvatura
Ricci = sp.Matrix([[0, 0, 0, 0],
                   [0, 2*Gamma_xxt.diff(x) + Gamma_yyt.diff(y) + Gamma_zzt.diff(z) - Gamma_xxy.diff(y) - Gamma_xxz.diff(z) - Gamma_yyx.diff(x) - Gamma_yyz.diff(z) - Gamma_zzx.diff(x) - Gamma_zzy.diff(y), 0, 0],
                   [0, 0, 2*Gamma_yyx.diff(y) + Gamma_xxt.diff(x) + Gamma_zzt.diff(z) - Gamma_xxy.diff(x) - Gamma_yyt.diff(x) - Gamma_yyz.diff(z) - Gamma_zzy.diff(y) - Gamma_zzx.diff(z), 0],





