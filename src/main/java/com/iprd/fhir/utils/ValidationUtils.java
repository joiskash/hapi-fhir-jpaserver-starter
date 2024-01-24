package com.iprd.fhir.utils;

import ca.uhn.fhir.context.FhirContext;
import ca.uhn.fhir.validation.FhirValidator;
import ca.uhn.fhir.validation.IValidatorModule;
import ca.uhn.fhir.validation.SingleValidationMessage;
import ca.uhn.fhir.validation.ValidationResult;
import org.hl7.fhir.common.hapi.validation.validator.FhirInstanceValidator;
import org.hl7.fhir.instance.model.api.IBaseResource;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ValidationUtils {

	private static final Logger logger = LoggerFactory.getLogger(ValidationUtils.class);

	public static void validateFhirResource(IBaseResource resource) {
		FhirContext ctx = FhirContext.forR4();
		FhirValidator validator = ctx.newValidator();
		IValidatorModule module = new FhirInstanceValidator(ctx);
		validator.registerValidatorModule(module);
		ValidationResult result = validator.validateWithResult(resource);

		for (SingleValidationMessage next : result.getMessages()) {
			logger.warn("Validation Error: " + next.getLocationString() + " " + next.getMessage());
		}
	}
}
