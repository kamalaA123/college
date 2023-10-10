function onChange(control, oldValue, newValue, isLoading, isTemplate) {
	if (isLoading || newValue === '') {
		return;
	}

	var url = 'https://www.google.com';
	if (confirm('If app not available in Teams App store , Please raise JIRA front door request using this link - ' + url)) {
		g_navigation.openPopup(url);
	}

}