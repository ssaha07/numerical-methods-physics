1. What are transcendental functions ?
->  Transcendental functions are those functions that cannot be represented algebraically and involve the solutions of 
    polynomial equations of finite degrees with rational coefficients. Such functions significantly differ from algebraic
    functions, like polynomials or rational functions, because they cannot be described using finite sequences of polynomial
    equations. E.g.:log x, sin x, cos x, ex and functions containing them.

2. Why use transcendental equations in astrophysics ?
-> Most of the basic and common astrophysical functions are transcendental, for e.g.:
    i)  gravity, g ∝ (distance)^-2
    ii) Stefan-Boltzmann Law, 𝐸 = 𝜎𝑇^4
    iii) wave propagation, ∇²E - (1/c²)∂²E/∂t² = 0
    We cannot solve such equations by just plain algebra, the physics itself demands a transcendental form.

3. Why we need boundary conditions to solve and get solutions to mysterious astronomical questions ?
-> Astrophysical objects are rarely point-like. Stars, disks, jets, and galaxies have edges, surfaces, and asymptotic limits.
    Boundary conditions in astronomical objects are essential mathematical constraints used in simulations and theoretical
    models to define how physical quantities like temperature, pressure, and magnetic fields behave at the edges of a system. 
    These conditions are crucial for solving the complex differential equations that govern celestial bodies and ensuring the
    solutions are physically realistic. 
    
    i) A unique, physically meaningful solution is obtained for a specific model (e.g., a star of a certain mass and composition)
     that satisfies the laws of physics [1]. Without these conditions, the equations would have infinitely many possible 
     mathematical solutions, most of which have no physical relevance to the real universe.
    ii) Improvement in prediction power, for instance, applying the boundary condition that a star's surface temperature matches
     the surrounding space allows models to predict its observed color and brightness.
    For eg:
        Astroseismology

        The standard Strum-Liouville-type equations are of form :





        The stellar oscillation equations, when simplified under the Cowling approximation (neglecting the perturbation of the gravitational potential) and for adiabatic pulsations, can be reduced to a single second-order, Sturm–Liouville-type differential equation for a scaled variable, often related to the pressure perturbation \(\psi \). 

        The equation of wave propagation for stellar acoustic oscillations (p-modes) in Sturm–Liouville–type :
        
        $\frac{d}{dr}(P(r)\frac{d\eta_r}{dr})+Q(r)\eta_r=\omega^2\Sigma(r)\eta_r$

        
        
        where: \(\xi \) is the dimensionless radial displacement perturbation, related to the actual displacement \(\xi _{r}\) by \(\xi =\xi _{r}/r\).\(P(r)=\Gamma _{1}P\rho ^{-1}r^{4}\) (after some steps, this can be written as \(\Gamma _{1}Pr^{4}\) in one common formulation) is the weight function for the derivative term.\(Q(r)=(3\Gamma _{1}-4)\rho gr^{4}\) is the potential term (or part of it).\(\lambda =\omega ^{2}\) is the eigenvalue, representing the square of the angular frequency of the oscillation.\(W(r)=\rho r^{4}\) is the weight function (or density) associated with the eigenvalue term. 

    Any Strum-Liouville-type equations can be further simplified, in this case, a particular tangent function appears in the wave equation when we solve for the eigen values. 

    The tangent function is equivalent to :
    tan (theta + phi) = const
    After applying surface boundary condition at r = R:
        tan (kR) = kR
        where, kR: wavelength fitting inside the star
    Hence, this is the key transcendental equation.
    It cannot be solved algebraically. The allowed oscillation frequencies are given by the numerical roots of this equation.

    One can solve other key transcendental equations using the functions in this project. Some of the sample transcendental equations are:
    i. x = tan x
    ii. x = a + b.sinh(x)
    iii. a = x^n.e^(-x)
    iv. x + ln(x) = a


