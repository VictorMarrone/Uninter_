package empresa;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args) throws Exception {
        int peso;
        double altura;

        System.out.println("Digite peso seguido de altura: ");
        Scanner teclado = new Scanner(System.in);
        peso = teclado.nextInt();
        altura = teclado.nextDouble();

        double imc = peso / (altura * altura);
        System.out.printf("Seu IMC: %.2f\n", imc);

        teclado.close();
    }
}
