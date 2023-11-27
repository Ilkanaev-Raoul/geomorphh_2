import math

def B_stern_form_M(rho_s, rho, Q_stern, C_stern, mu_strich):
    B_stern = 28.1*((rho_s/rho)-1)**(-0.5) * Q_stern**(0.5) * C_stern**(-1.12) * mu_strich**(-1.66)
    return B_stern
def D_stern_form_M(rho_s, rho, Q_stern, C_stern, mu_strich):
    D_stern = 0.0764((rho_s / rho) - 1) ** (-0.37) * Q_stern ** (0.37) * C_stern ** (1.16) * mu_strich ** (1.22)
    return D_stern
def Jf_form_M(rho_s, rho, Q_stern, C_stern, mu_strich):
    Jf = 1.98((rho_s / rho) - 1) ** (0.33) * Q_stern ** (-0.33) * C_stern ** (-1.86) * mu_strich ** (-0.93)
    return Jf

def Q_stern_form(Q, g, d50):
    Q_stern = Q/(math.sqrt(g*d50**5))
    return Q_stern

def B_form(B_stern, d50):
    B_M = B_stern*d50
    return B_M

def D_form(D_stern, d50):
    D_M = D_stern*d50
    return D_M

def C_stern_form:
    C_stern = -math.log((rho_s*Q_s)/(rho*Q))
    return C_stern






rho = 1000
rho_s = 1600
d50 = 1e-3
Q = 1500
g = 9.81
mu_strich = 1.4
B = 300
Q_s = 0.0123

