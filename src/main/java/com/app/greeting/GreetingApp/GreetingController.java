package com.app.greeting.GreetingApp;

import java.util.Date;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {
	
	@RequestMapping("/getGreeting")
	public String getGreeting() {
		
		return "Hello AWS_CICD_Pipelines";
	}
	
	@RequestMapping("/getDate")
	public String getDate() {
		return new Date().toString();
	}

}
