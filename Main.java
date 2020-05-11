package net.codejava;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		//Person Variables
		
		//Architect
	String archName;
	String archPhoneNum;
	String archEmail;		
	String archAddress;
		
		//Contractor
	String contName;
	String contPhoneNum;
	String contEmail;
	String contAddress;
	
		//Customer
	String custName;
	String custPhoneNum;
	String custEmail;
	String custAddress;
	
		//Project Variables
	Project project = null;
	String projectNum;
	String projectName;
	String buildType;
	String buildAddress;
	String ERFNum;
	double totalFee;
	double amountPaidDate;
	String deadline; 
		
	boolean running = true;
	Scanner input = new Scanner(System.in);
	while(running) {
		//Menu
		System.out.println("\nCP - Create New Project\n"
				+ "CD - Change the Projects Due Date\n" 
				+ "CA - Change the Total Amount Paid to Date\n"
				+ "UC - Update the Contractors Details\n"  
				+ "E - Exit program");
		
		//Menu Input
		String choice = input.nextLine();
		
		//Create Project
		if(choice.equalsIgnoreCase("cp")) {
			System.out.println("Project Number: ");
			projectNum = input.nextLine();
			
			System.out.println("Building Type: ");
			buildType = input.nextLine();
					
			System.out.println("Project Name: ");
			projectName = input.nextLine();
			
			System.out.println("Building Address: ");
			buildAddress = input.nextLine();
						
			System.out.println("ERF number: ");
			ERFNum = input.nextLine();
			
			System.out.println("Total Fee: ");
			totalFee = input.nextDouble();
			
			System.out.println("Total Paid to Date: ");
			amountPaidDate = input.nextDouble();
			
			System.out.println("Project Deadline: ");
			deadline = input.nextLine();
			
			//Architect 
			System.out.println("\nArchitects Details:");
			System.out.print("Name: ");
			archName = input.nextLine();
			System.out.print("Phone Number: ");
			archPhoneNum = input.nextLine();
			System.out.print("Email Address: ");
			archEmail = input.nextLine();
			System.out.print("Physical Address: ");
			archAddress = input.nextLine();
			//Creating Architect Object
			Person architect = new Person("Architect", archName, archPhoneNum, archEmail,archAddress);
			
			//Customer
			System.out.println("\nCustomer Details:");
			System.out.print("Name: ");
			custName = input.nextLine();
			System.out.print("Phone Number: ");
			custPhoneNum = input.nextLine();
			System.out.print("Email Address: ");
			custEmail = input.nextLine();
			System.out.print("Physical Address: ");
			custAddress = input.nextLine();
			//Creating Customer Object
			Person customer = new Person("Customer", custName, custPhoneNum, custEmail,custAddress);
			
			//Contractor
			System.out.println("\nContractor Details:");
			System.out.print("Name: ");
			contName = input.nextLine();
			System.out.print("Phone Number: ");
			contPhoneNum = input.nextLine();
			System.out.print("Email Address: ");
			contEmail = input.nextLine();
			System.out.print("Physical Address: ");
			contAddress = input.nextLine();
			//Creating Contractor Object
			Person contractor = new Person("Contractor", contName, contPhoneNum, contEmail, contAddress);
			
			//Creating Project Object
			if(projectName.equalsIgnoreCase("")) {
				projectName = custName + " " + buildType;
			}
			
			project = new Project(projectNum,projectName,buildType,buildAddress,ERFNum,amountPaidDate,totalFee,deadline,architect,customer,contractor);
			
			//Successful Output
			System.out.println("\nProject Succesfully Created!");
			
			project.toString();
		}
		//Change Projects Deadline:
		if(choice.equalsIgnoreCase("CD")) {
			if(project == null) {
				System.out.println("No Project Found!");
			} else
			project.changeDate();
			project.toString();
		}
		//Change Total Paid to Date:
		if(choice.equalsIgnoreCase("CA")) {
			if(project == null) {
				System.out.println("No Project Found!");
			} else
			project.changeAmountPaid();
			project.toString();
		}
		//Update Contractor Details:
		if(choice.equalsIgnoreCase("UC")) {
			if(project == null) {
				System.out.println("No Project Found!");
			} else
			project.updateContractor();
			project.toString();
		}		
		//Exit
		if(choice.equalsIgnoreCase("E")) {
			running = false;
		}
	}
	input.close();
 }	
}
