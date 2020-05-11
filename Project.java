package net.codejava;

import java.util.*;
import java.time.*;

public class Project {
	//Variable|Constructors
	String projectNum;
	String projectName;
	String buildType;
	String buildAddress;
	String ERFNum;
	double totalFee;
	double amountPaidDate;
	String deadline;
	String projectFinalized;
	Person architect;
	Person contractor;
	Person customer;
	//Constructor
	public Project(String projectNum,String projectName,String buildType,String buildAddress,String ERFNum,double totalFee,double amountPaidDate,
				   String deadline,Person architect,Person customer,Person contractor) {
		
		this.projectNum = projectNum;
		this.projectName = projectName;
		this.buildType = buildType;
		this.buildAddress = buildAddress;
		this.ERFNum = ERFNum;
		this.totalFee = totalFee;
		this.amountPaidDate = amountPaidDate;
		this.deadline = deadline;
		//this.projectFinalized = projectFinalized;
		this.architect = architect;
		this.contractor = contractor;
		this.customer = customer;
	}
	//Methods
	Scanner input = new Scanner(System.in);
	//Print out Project Details Method
	public void displayProject() {
		String projectDetails = "Project Number: " + projectNum;
		projectDetails += "\nProject Name: " + projectName;
		projectDetails += "\nBuilding Type: " + buildType;
		projectDetails += "\nSite Address: " + buildAddress;
		projectDetails += "\nERF Number: " + ERFNum;
		projectDetails += "\nTotal Fee: R" + totalFee;
		projectDetails += "\nTotal amount paid to date: R" + amountPaidDate;
		projectDetails += "\nDeadline of Project: " + deadline;
		projectDetails += "\nProject Finalized: " + projectFinalized;
		
		//Output
		System.out.println(projectDetails);
		architect.toString();
		contractor.toString();
		customer.toString();	
	}
	//Change the Due Date Method
	public void changeDate() {
		System.out.println("What would you like the new deadline to be? ");
		String newDate = input.next();
		this.deadline = newDate;
		System.out.println("The deadline has been updated!");
	}
	//Change the Total Paid to Date:
	public void changeAmountPaid() {
		System.out.println("How much has been paid to date? ");
		input.nextLine();
		double newAmount = input.nextDouble();
		this.amountPaidDate = newAmount;
		System.out.println("Amount Paid to Date Updated!");
	}
	//Update the Contractors Details
	public void updateContractor() {
		//Verify if the Phone Number needs to be Updated.
		System.out.println("Update the Contractors Phone Number? Yes/ No");
		String choice = input.nextLine();
		if(choice.equalsIgnoreCase("Yes")) {
			System.out.println("Phone Number: ");
			String newPhoneNum = input.next();
			this.contractor.phoneNum = newPhoneNum;
			System.out.println("Phone Number Updated!");
		}
		//Verify if the Email Address needs to be Updated.
		System.out.println("Update the Contractors Email Address? Yes/ No");
		choice = input.next();
		if(choice.equalsIgnoreCase("Yes")) {
			System.out.println("Email Address: ");
			String newEmail = input.next();
			this.contractor.emailAddress = newEmail;
			System.out.println("Email Address Updated!");
		}
	}
}

