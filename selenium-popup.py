    main_window = browser.current_window_handle
    all_links = browser.find_elements_by_css_selector('img[src="lupa.png"]')

    all_links[0].click()
    # POPUP SWITCH
    windows = browser.window_handles
    browser.switch_to.window(windows[1])
    time.sleep(3)
    print(browser.find_element_by_css_selector('.tablaPop tbody tr:nth-of-type(2)').text)
    browser.close()

    # MAIN WINDOW RETURNS
    browser.switch_to.window(main_window)
