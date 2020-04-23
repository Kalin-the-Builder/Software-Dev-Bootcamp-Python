package net.codejava;

public class Project {
	int projectNum;
	String projectName;
	String buildType;
	String siteAddress;
	int ERF;
	double totalFee;
	double amountOutstanding;
	String deadline;
	String projectFinalized;
	
	public Project(int projectNum,String projectName,String buildType,String siteAddress,int ERF,double totalFee,double amountOutstanding,String deadline,String projectFinalized) {
		this.projectNum = projectNum;
		this.projectName = projectName;
		this.buildType = buildType;
		this.siteAddress = siteAddress;
		this.ERF = ERF;
		this.totalFee = totalFee;
		this.amountOutstanding = amountOutstanding;
		this.deadline = deadline;
		this.projectFinalized = projectFinalized;
	}
	public int getProjectNum() {
		return projectNum;
	}
	public String getProjectName() {
		return projectName;
	}
	public int getERF() {
		return ERF;
	}
	public double getTotalFee() {
		return totalFee;
	}
	public double getAmountOutstanding() {
		return amountOutstanding;
	}
	public String getDeadline() {
		return deadline;
	}
	public String getProjectFinalized() {
		return projectFinalized;
	}
	public String toString() {
		String output = "Project Number: " + projectNum;
		output += "\nProject Name: " + projectName;
		output += "\nBuilding Type: " + buildType;
		output += "\nSite Address: " + siteAddress;
		output += "\nERF Number: " + ERF;
		output += "\nTotal Fee: R" + totalFee;
		output += "\nTotal amount paid to date: R" + amountOutstanding;
		output += "\nDeadline of Project: " + deadline;
		output += "\nProject Finalized: " + projectFinalized;
		
		return output;
	}
		
}

