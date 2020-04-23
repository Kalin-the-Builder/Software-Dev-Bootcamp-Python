package net.codejava;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

	Scanner scanner = new Scanner(System.in);
	
	System.out.println("Enter the Project Number?\n");
	int projectNum = scanner.nextInt();
	
	System.out.println("Enter the Building Type?\n");
	String buildType = scanner.nextLine();
	
	System.out.println("Enter the Project Name?\n");
	String projectName = scanner.next();
	scanner.nextLine();
	if(projectName == "") {
		String customerName = Customer.getName(); //This should get the customer name. 
		projectName = buildType + " " + customerName; 
	}
	System.out.println("Enter the Site Address?\n");
	String siteAddress = scanner.nextLine();
	
	System.out.println("Enter the ERF number?\n");
	int ERF = scanner.nextInt();
	
	System.out.println("Enter the Total Fee?\n");
	double totalFee = scanner.nextDouble();
	
	System.out.println("How much has been paid to date?\n");
	double amountOutstanding = scanner.nextDouble();
	amountOutstanding = totalFee - amountOutstanding;
	
	System.out.println("Enter the deadline of the Project?\n");
	String deadline = scanner.next();
	scanner.nextLine();
	
	String projectFinalized = "";
	
	Project projectTest = new Project(projectNum,projectName,buildType,siteAddress,ERF,totalFee,amountOutstanding,deadline,projectFinalized);
	
	System.out.println("Project:\n");
	System.out.println(projectTest.toString());
	
	Architect architectTest = new Architect("Name","000 000 0000","name@domain.co.za","Cape Town");
	
	Contractor contractorTest = new Contractor("Name","000 000 0000","name@domain.co.za","Cape Town");
	
	Customer customerTest = new Customer("Name","000 000 0000","name@domain.co.za","Cape Town");
	
	System.out.println("\nArchitect:\n");
	System.out.println(architectTest.toString());
	
	System.out.println("\nContractor:\n");
	System.out.println(contractorTest.toString());
	
	System.out.println("\nCustomer:\n");
	System.out.println(customerTest.toString());
	//Change Due Date:
	System.out.println("Would you like to change the due date of the project? Yes/ No");
	String choice = scanner.nextLine();
	if(choice == "Yes") {
		System.out.println("What is the new due date of the project? ");
		deadline = scanner.next();
		System.out.println(projectTest.toString());
	} //Change the amount paid to date:
	System.out.println("Would you like to change the total amount paid to date? Yes/ No");
	choice = scanner.nextLine();
	if(choice == "Yes") {
		System.out.println("What is the total amount paid up to date? ");
		amountOutstanding = scanner.nextInt();
		amountOutstanding = totalFee - amountOutstanding;
		System.out.println(projectTest.toString());
	} //Update Contractor's Contact Details:
	System.out.println("Please updare the contact number of the contractor?\n");
	String contactNum = scanner.nextLine();
	
	System.out.println("Please update the email address of the contractor?\n");
	String emailAddress = scanner.next();
	Contractor contractorUpdate = new Contractor("Name",contactNum,emailAddress,"Cape Town");
	
	
	System.out.println("\nContractor\n");
	System.out.println(contractorUpdate.toString());
	 //Finalize the Project:
	System.out.println("Has the project been finalized?'n");
	choice = scanner.next();
	if(choice == "Yes") {
		projectFinalized = "Completed Project";
		System.out.println(projectTest.toString());
		}
	}
}
