

# Calculate the total savings you can get from a starting annualSalary
def f():
    annualSalary = 80000
    global timeWorking 
    timeWorking= 20
    annualSalaryIncrease = 5000
    super = 0.1 # Superannuation
    annualSavingPercent = 0.1
    tax = 0.04
    totalSaving = annualSalary*(super+annualSavingPercent-tax)
    annualROI = 1.1
    
    # Calculating part
    for i in range(1, timeWorking+1):
        if (i == 1): 
            annualSaving = annualSalary*(super+annualSavingPercent-tax)
            totalSaving = annualSaving
        else: 
            # The savings includes superannuation + personal savings - tax
            annualSalary += annualSalaryIncrease        
            annualSaving = annualSalary * (super+annualSavingPercent-tax)
            totalSaving = totalSaving * annualROI + annualSaving
        
        print('year:', i, '/ annualSalary:', annualSalary, '/ annualSaving:',annualSaving, '/ totalSaving:', totalSaving)      
    return totalSaving


print('You have saved', f(), 'after', timeWorking, 'years working.')