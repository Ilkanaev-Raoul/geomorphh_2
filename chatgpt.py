import math

def B_stern_form_M(rho_s, rho, Q_stern, C_stern, mu_strich):
    B_stern = 28.1 * ((rho_s / rho) - 1) ** (-0.5) * Q_stern ** (0.5) * C_stern ** (-1.12) * mu_strich ** (-1.66)
    return B_stern

def D_stern_form_M(rho_s, rho, Q_stern, C_stern, mu_strich):
    D_stern = 0.0764 * ((rho_s / rho) - 1) ** (-0.37) * Q_stern ** (0.37) * C_stern ** (1.16) * mu_strich ** (1.22)
    return D_stern

def Jf_form_M(rho_s, rho, Q_stern, C_stern, mu_strich):
    Jf = 1.98 * ((rho_s / rho) - 1) ** (0.33) * Q_stern ** (-0.33) * C_stern ** (-1.86) * mu_strich ** (-0.93)
    return Jf

def Q_stern_form(Q, g, d50):
    Q_stern = Q / (math.sqrt(g * d50 ** 5))
    return Q_stern

def B_form(B_stern, d50):
    B_M = B_stern * d50
    return B_M

def D_form(D_stern, d50):
    D_M = D_stern * d50
    return D_M

def C_stern_form(rho_s, rho, Q_s, Q):
    C_stern = -math.log((rho_s * Q_s) / (rho * Q))
    return C_stern

def B_stern_P(Q_stern):
    return 4.63 * Q_stern ** (0.4667)

def D_stern_P(Q_stern):
    return 0.382 * Q_stern ** (0.3996)

# Combined function
def combined_function(rho_s, rho, Q, Q_s, g, d50, mu_strich):
    Q_stern = Q_stern_form(Q, g, d50)
    C_stern = C_stern_form(rho_s, rho, Q_s, Q)
    B_stern = B_stern_form_M(rho_s, rho, Q_stern, C_stern, mu_strich)
    D_stern = D_stern_form_M(rho_s, rho, Q_stern, C_stern, mu_strich)
    B_M = B_form(B_stern, d50)
    D_M = D_form(D_stern, d50)
    B_P = B_stern_P(Q_stern) * d50
    D_P = D_stern_P(Q_stern) * d50
    return B_stern, D_stern, B_M, D_M, B_P, D_P

# Print function with results including B_P and D_P
def print_results(rho_s, rho, Q, Q_s, g, d50, mu_strich):
    B_stern, D_stern, B_M, D_M, B_P, D_P = combined_function(rho_s, rho, Q, Q_s, g, d50, mu_strich)
    print(f"B_stern (Dimensionless width parameter): {B_stern:.4f}")
    print(f"D_stern (Dimensionless depth parameter): {D_stern:.4f}")
    print(f"B_M (Width in meters): {B_M:.4f} m")
    print(f"D_M (Depth in meters): {D_M:.4f} m")
    print(f"B_P (Width prediction in meters): {B_P:.4f} m")
    print(f"D_P (Depth prediction in meters): {D_P:.4f} m")

# Example usage
# Replace the placeholders with actual values before running the function
# print_results(rho_s, rho, Q, Q_s, g, d50, mu_strich)

rho = 1000
rho_s = 1600
d50 = 1e-3
Q = 1500
g = 9.81
mu_strich = 1.4
B = 300
Q_s = 0.0123

print_results(rho_s, rho, Q, Q_s, g, d50, mu_strich)