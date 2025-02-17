package empresa;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) throws Exception {
        

        // Primitivas
        // int, float, double, char letra = 'd';
        Scanner teclado = new Scanner(System.in);


        ArrayList<String> listaNomes = new ArrayList<String>();
        System.out.println("Digite a quantidade de nomes:");
        int qtd=  teclado.nextInt();
        String nome;
        for (int i=0; i<qtd; i++) {
            nome = teclado.next();
            listaNomes.add(nome);
            
        }

        
        System.out.println("Ordem normal:");
        System.out.println(listaNomes);

        Collections.reverse(listaNomes);

        System.out.println("Ordem reversa: ");
        System.out.println(listaNomes);

       /*  for (int i=listaNomes.size()-1; i>=0; i--) {
            System.out.println(listaNomes.get(i));
        } */

        teclado.close();
    }
}
