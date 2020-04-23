package net.codejava;

public class Customer {
		//Attributes
	String name;
	String telephoneNum;
	String emailAddress;
	String physicalAddress;
		//Methods
	public Customer(String name,String telephoneNum,String emailAddress,String physicalAddress) {
		this.name = name;
		this.telephoneNum = telephoneNum;
		this.emailAddress = emailAddress;
		this.physicalAddress = physicalAddress;
	}
	public String getName() {
		return name;
	}
	public String getTelephoneNum() {
		return telephoneNum;
	}
	public String getEmailAddress() {
		return emailAddress;
	}
	public String toString() {
		String output = "Name: " + name;
		output += "\nTelephone Number: " + telephoneNum;
		output += "\nEmail Address: " + emailAddress;
		output += "\nPhysical Address: " + physicalAddress;
		
		return output;
	}
}
