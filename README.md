# Platypus
A simple Python library made to facilitate the easy generation of two-dimensional, procedurally-generated terrains and maps.

##### Includes:
- A function to generate two-dimensional terrains given a width, height, smoothness, and a dictionary of terrain values.
- A function to easily display terrains generated by Platypus.

## Usage
To generate a new terrain, simply call the `platypus.generate` function.

`platypus.generate` takes four arguments:
1. `width`: The width of the terrain to generate.
2. `height`: The height of the terrain to generate.
3. `smoothness`: The number of times to iterate over and smooth the terrain.
   - This should be an integer >= 0.
   - If `smoothness` is a small value, the terrain will be more noisy. This is good for small terrains, but can be chaotic for large ones.
   - If `smoothness` is a large value, the terrain will be more smoothly-bordered. This is great for large terrains, but can result in overly-simplified small terrains.
4. `values`: A dictionary of terrain values (characters, text, objects, doesn't matter!) paired to their relative likelihoods to appear.
   - This should be formatted as so: `{*value*: *likelihood*, *value*: *likelihood*, ...}`
   - The likelihoods to appear are all relative -- they don't have to add up to 1 (or 100, for that matter). One could write a `values` dictionary like so: `{"#": 3, "%": 2}` and it would only mean that "%" is 2/3 as likely to appear as "#".

## Examples
Running this code:
```python
terrain = platypus.generate(10, 10, 1, {"#": 1, " ": 1})
platypus.display_terrain(terrain)
```
...can lead to this output:
```
            #  #  #  #        
            #  #  #  #        
#  #           #  #  #        
#  #              #           
#                             
#  #           #              
#  #  #     #  #  #        #  
#              #  #  #  #  #  
                  #  #  #  #  
                     #  #  #  
```

...and running *this* code:
```python
terrain = platypus.generate(80, 40, 10, {"X": 0.2442, "#": 0.2558, ".": 0.2442, " ": 0.2558})
platypus.display_terrain(terrain)
```

...can lead to *this* output:
```
#  #  #  #  #                                                                       #  #  #  #  #  #  #                 #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  X  X  X  X  #  #  #  #  #  #  #  #  #  .  .  .  .  X  X  X  X  X  X  X  X  
#  #  #  #                                                                       #  #  #  #  #  #  #  #                 #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  X  X  X  X  #  #  #  #  #  #  #  #  #  .  .  .  .  X  X  X  X  X  X  X  X  
#  #  #                                                                          #  #  #  #  #  #  #  #  #        #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  X  X  X  X  #  #  #  #  #  #  #  #  #  .  .  .  .  X  X  X  X  X  X  X  X  
                                                                                 #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .        X  X  #  #  #  #  #  #  #  #  #  #  .  .  .  X  X  X  X  X  X  X  X  X  
                                                                              #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                       #  #  #  #  #  #  #  #  #  #  #  .  X  X  X  X  X  X  X  X  X  X  
                                                                           #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                          #  #  #  #  #  #  #  #  #  #     X  X  X  X  X  X  X  X  X  X  
#  #  #  #  #  #  #  #                                                  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                             #  #  #  #  #  #  #  #           X  X  X  X  X  X  X  X  X  
#  #  #  #  #  #  #  #  #  #                                         #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                   #  #  #  #  #  #  #              X  X  X  X  X  X  X  X  
#  #  #  #  #  #  #  #  #  #  #           .  .  .  .  .  .  .     #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                         #  #  #  #  #  #              X  X  X  X  X  X  X  X  
#  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  X  X  X  X  X  X                                         #  #  #  #  #                 X  X  X  X  X  X  X  
#  #  #  X  X  X  #  #  #  #  .  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  X  X  X  X  X  X  X  X  X                                      #  #  #  #  #                 X  X  X  X  X  X  X  
X  X  X  X  X  X  X  X  #  .  .  .  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  X                                   #  #  #  #  X  X              X  X  X  X  X  X  X  
X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .  .  .  .                    #  #  #  #  #  #  #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X                                      #  #  X  X  X  X  X  X     X  X  X  X  X  X  X  
X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .  .                       #  #  #  #  #  #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X                                   X  X  X  X  X  X  X  X  X  X  X  X  #  #  #  #  
X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .                             #  #  #  #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X                                X  X  X  X  X  X  X  X  X  X  X  #  #  #  #  #  
X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .                                #  #  #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X     #  #                 .  X  X  X  X  X  X  X  X  X  X  X  #  #  #  #  #  
X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  .                                #  #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  #  #  #  #  #     .  .  .  .  X  X  X  X  X  X  X  X  X  X  #  #  #  #  #  
X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .                                   #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  #  #  #  #  .  .  .  .  .  .  X  X  X  X  X  X  X  X        #  #  #  #  
X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .                                   #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  X  .  .  X  X  X  X  X  X  X  X  X  X  X  #  .  .  .  .  .  .  .  .  X  X  X  X  X  X                       
X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .                                   #  #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .  X  X  X  X  X                          
X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .                                   #  #  #  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  X  X  X  X  X                             
X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .                                   .  .  .  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  X  X  X  X  X                                
X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .  .                             .  .  .  .  .  X  X  X  X  X  X  X  X  X  #  #  .  .  .  .  .  .  X  X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  X  X  X  X                                   
X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .                          .  .  .  .  .  .  .  X  X  X  X  X  X  X  #  #  #  #  .  .  .  .  .  X  X  X  X  X  X  X  X  X  X  X  X  #  #  #  #  #  X  X                                      
X  X  X  X  X  X  X  X  X  X  X  .  .  .  .  .  .  .                       .  .  .  .  .  .  .  .  .  X  X  X  X  X  #  #  #  #  #  #  .  .  .  .  X  X  X  X  X  X  X  X  X  X  X  #  #  #  #  #  #  #                                         
X  X  X  X  X  X  X  X  X  #  #  #  #  #  .  .  .                       .  .  .  .  .  .  .  .  .  .  .  .  .  X  #  #  #  #  #  #  #  #  #  .  #  #  X  X  X  X  X  X  X  X  X  #  #  #  #  #  #  #  #                                         
X  X  X  X  X  X  X  X  #  #  #  #  #  #  #  .  .                       .  .  .  .  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  X  X  X  X  X  #  #  #  #  #  #  #  #  #  #                                         
      X  X  X  X  #  #  #  #  #  #  #  #  #  #                          .  .  .  .  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                         
            X  #  #  #  #  #  #  #  #  #  #  #  #  #  #              #  .  .  .  .  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                         
               #  #  #  #  #  #  #  #  #  #  #  #  #  #  #        #  #  #  .  .  .  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                         
               #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                         
               #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                            
                  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #                                            
                  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .                                         
                     #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .        X  X                          
                  X  X  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  #  #  #  #  #  X  X  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  X  X  X  X                       
               X  X  X  X  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  #  #  X  X  X  X  X  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  X  X  X  X  X  X                    
            X  X  X  X  X  X  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  X  X  X  X  X  X  X  #  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  X  X  X  X  X  X     #  #  #  #  
            X  X  X  X  X  X  X        #  #  #  #  #  #  #  #  .  .  .  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  X  X  X  X  X  X  X  X  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  X  X  X  X  X  X  #  #  #  #  #  
            X  X  X  X  X  X              #  #  #  #  #  X  #  .  .  .  .  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  X  X  X  X  X  X  X  X  #  #  #  #  #  #  #  #  #  #  #  .  .  .  .  .  .  .  .  X  X  X  X  X  X  #  #  #  #  #
```
## Installation
### Requirements:
- Python 3 (developed with Python 3.6.5)

### Manual Install:
At the moment, Platypus is not available on PyPI or for installation with distutils. For now, just copy the platypus.py file into your working directory.

## Potential Future Features
- "Sprinkle" values
  - Another set of values can be optionally passed into `platypus.generate()` to place individual points on the map after the terrain values are placed.
  - Especially useful for point locations as opposed to regions (e.g. cities, mines, special plants, etc. as opposed to forests, lakes, countries, etc.).
- Callback detection
  - Platypus checks to see if passed values are callbacks, and if so, waits until smoothing is done to call them.
  - If a user wanted to generate each tile's properties individually upon construction, this functionality would provide for it.
  - This is useful if values are callbacks to randomly-influenced object constructors.
- distutils installation
  
