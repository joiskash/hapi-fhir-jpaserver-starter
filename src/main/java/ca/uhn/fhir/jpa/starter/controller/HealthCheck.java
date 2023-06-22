package ca.uhn.fhir.jpa.starter.controller;

import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;

@Component("myHealthCheck")
public class HealthCheck implements HealthIndicator {

	@Override
	public Health health() {
		System.out.println("HEALTH is hitttttttttttttttttttttttttttt-----------------------------------------------");
		return Health.up().build();
	}
}