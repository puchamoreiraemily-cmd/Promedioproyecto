/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.promedioproyecto;

/**
 *
 * @author HP
 */
public class Promedioproyecto {

    public static double calcularPromedio(double nota1, double nota2) {
        double promedio = (nota1 + nota2) / 2;
        return promedio;
    }

    public static void main(String[] args) {

        double nota1 = 8.5;
        double nota2 = 9.5;

        double resultado = calcularPromedio(nota1, nota2);

        System.out.println("El promedio es: " + resultado);
    }
}
   
