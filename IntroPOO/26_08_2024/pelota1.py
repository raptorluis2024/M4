class Pelota():
# Método de instancia que asigna color

    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color
        # Método de instancia que lee color de la instancia
    def lee_color(self):
        print("El color de esta pelota es {}".format(self.color))
        
    def lee_color_local_y_atributo(self, color_local: str):
        # Esta variable "color" sólo existe en el alcance del método
        color = color_local
        # Un método de instancia puede llamar a otros métodos
        if self.color != color:
           print("El color {} NO es el color de ESTA pelota".format(color))
        else:
            print("El color {} SI es el color de ESTA pelota".format(color))
            
    def comparar_colores(self, other):
        if self.color == other.color:
            print("ambas pelotas tienen el mismo color")
        else:
            print("las pelotas no tienen el mismo color")