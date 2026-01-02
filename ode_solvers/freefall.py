import matplotlib.pyplot as plt
from .euler import euler
from .rk4 import runge_kutta


def main():
    print("NUMERICAL SOLUTION OF ORDINARY DIFFERENTIAL EQUATION")
    print("Problem: Free Fall with Linear Air Resistance")

    # ------ Physical Parameters ------

    m = float(input("Enter mass of object : "))
    k = float(input("Enter linear drag coefficient (in kg/s) : "))
    g = 9.81  #gravitational acceleration (m / s^2)

    def f(t, v):
        return g - (k / m) * v
    # ----- Initial Conditions -----
    x0 = 0.0      # initial time (s)
    y0 = 0.0      # initial velocity (m/s)
    h = 0.01      # step size 
    N = 2000      # number of steps
    # ----- For Energy Conservation -----
    
    K = []
    U = []
    E = []
    


    # ----- RK4 Solution -----
    res_rk4 = runge_kutta(f, x0, y0, h, N)
    t_vals = [i[0] for i in res_rk4]
    v_vals = [i[1] for i in res_rk4]
    y_vals = [0.0]       # initial position
    
    for i in range(1, len(t_vals)):
        y_next = y_vals[-1] + v_vals[i - 1] * h
        y_vals.append(y_next)
    K = [0.5 * m * v ** 2 for v in v_vals]
    U = [m * g * (-y) for y in y_vals]
    E = [K[i] + U[i] for i in range(len(K))]
    # ----- Print Output -----
    print("------ RUNGE-KUTTA METHOD -------")
    print(f"{'t (s)' :<10}{'v (m/s)':<15}")
    print("-" * 25)
    for i in range (0, len(t_vals), 200):
        print(f"{t_vals[i]:<10.2f}{v_vals[i]:<15.3f}")
    print("\nFinal velocity =", f"{v_vals[-1]:.3f}", "m/s")
    print("\n\n")
    

    # ---- Plot RK4 ----
    plt.figure()
    plt.plot(t_vals, v_vals)
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Free fall with Linear Air Resistance (RK4)")
    plt.grid(True)
    plt.savefig("v_vs_t_rk4.png", dpi=300, bbox_inches="tight")

    # ---- Euler Solution ----
    res_euler = euler(f, x0, y0, h, N)
    t_val = [j[0] for j in res_euler]
    v_val = [j[1] for j in res_euler]

    # ---- Print Output ----
    print("------ EULER METHOD ------")
    print(f"{'t (s)':<10}{'v (m/s)':<15}")
    print("-" * 25)
    for i in range (0, len(t_val), 200):
        print(f"{t_val[i]:<10.2f}{v_val[i]:<15.3f}")
    print("\nFinal velocity =", f"{v_val[-1]:.3f}", "m/s")
    print("\n\n")

    # ----Energy Analysis----
    print(f"{'t (s)':<10}{'Kinetic (J)':<15}{'Potential (J)':<15}{'Total (J)':<15}")
    print("-" * 55)
    for i in range(0, len(t_vals), 200):
        print(f"{t_vals[i]:<10.2f}{K[i]:<15.3f}{U[i]:<15.3f}{E[i]:<15.3f}")
    plt.figure()
    plt.plot(t_vals, K, color = 'red', label = "Kinetic Energy")
    plt.plot(t_vals, U, color = 'blue', label = "Potential Energy")
    plt.plot(t_vals, E, color = 'green', label = "Total Energy")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.title("Energy vs Time (with Linear Air Resistance)")
    plt.legend()
    plt.grid(True)
    plt.savefig("energy_vs_time.png", dpi=300, bbox_inches="tight")

    # ---- Plot Euler -----
    plt.figure()
    plt.plot(t_val, v_val)
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.title("Free fall with Linear Air Resistance (Euler)")
    plt.grid(True)
    plt.savefig("v_vs_t_euler.png", dpi=300, bbox_inches="tight")

if __name__ == "__main__":
    main()




    