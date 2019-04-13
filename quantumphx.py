
import numpy as np
import scipy as scp
import matplotlib.pyplot as plt

print('------------Welcome to my world of quantum physics!-------------')
print('------------------Here is your calculator-----------------------')
print('-------------------by Salman Al Farisi--------------------------\n')
print('Choose your option:')
print('1. Photon Energy')
print('2. Black Body Radiation')
print('3. Photon momentum')
print('4. de Broglie Wavelength')



choose = input('Select your number option: ')
h = 6.626e-34
c = 3.0e+8
k = 1.38e-23
eV = 6.242e+18 
if (choose=='1'): 
    print('\nyou have frequency or wavelength ? ')
    print('1. frequency (input in Hz)')
    print('2. wavelength (input in m)')
    lambdaorfreq = input('Choose input option: ')
    if (lambdaorfreq == '1'):
        def ph_energy_f(quanta,freq):
            E = (float(quanta)*h*freq)
            return E
        
        n = input('Enter your number of photon (default = 1): ')
        if (n == ''):
            n = float(1)
            f = float(input('Enter your frequency: '))
            energy = ph_energy_f(n,f)
            print('Photon energy = ',energy,' J')
            print('Photon energy = ',energy*eV, 'eV')
        else:
            if ((float(n) != int(float(n))) == True):
                print('n must be integer in quantization concept')
            else:     
                f = float(input('Enter your frequency: '))
                energy = ph_energy_f(n,f)
                print('Photon energy = ',energy,' J')
                print('Photon energy = ',energy*eV, 'eV')
            
            
    elif(lambdaorfreq == '2'):
        def ph_energy_l(quanta,l):
            E = float(n)*h*(c/l)
            return E
        
        n = input('Enter your number of photon (default = 1): ')
        if (n == ''):
            n = float(1)
            wl = float(input('Enter your wavelength (m): '))
            energy = ph_energy_l(n,wl)
            print('Photon energy = ',energy,' J')
            print('Photon energy = ',energy*eV, 'eV')
        else:
            if ((float(n) != int(float(n))) == True):
                print('n must be integer in quantization concept')
            else:
                wl = float(input('Enter your wavelength (m): '))
                energy = ph_energy_l(n,wl)
                print('Photon energy = ',energy,' J')
                print('Photon energy = ',energy*eV, 'eV')

elif (choose=='2'):
    Temperature = float(input("Temperature: "))
    def planck(wav, T):
        a = 2.0*h*c**2
        b = h*c/(wav*k*T)
        intensity = a/ ( (wav**5) * (np.exp(b) - 1.0) )
        return intensity
    
    
    wavelengths = np.arange(1e-9, 1e-6, 1e-9) 
    #adjust with your result if unconvenient
    
    
    intensity = planck(wavelengths, Temperature)
    intensity[0]=0
    
    
    plt.grid()
    plt.plot(wavelengths*1e9, intensity) 
    plt.xlabel('Wavelength (Angstorm)')
    plt.show()
    
elif(choose =='3'):
    def momentum_f(freq):
        p = (h*freq)/c
        return p
    def momentum_l(l):
        p = h/l
        return p
    print('\nyou have frequency or wavelength ? ')
    print('1. frequency (input in Hz)')
    print('2. wavelength (input in m)')
    lambdaorfreq = input('Choose input option: ')
    if (lambdaorfreq =='1'):
        f = float(input('Enter your frequency: '))
        momentum = momentum_f(f)
        
    elif (lambdaorfreq =='2'):
        wl = float(input('Enter your wavelength (m): '))
        momentum = momentum_l(wl)
        
    print('Photon momentum = ',momentum,'kg.m.s-1')
        
elif(choose == '4'):
    def db_wavelength(m,v):
        l = h/(m*v)
        return l

    mass = float(input('input object mass (kg): '))  
    velo = float(input('input object velocity (m/s): ')
    
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        