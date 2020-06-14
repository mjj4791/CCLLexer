%#IFNDEF HELLO_WORLD                                ; conditional includes
%#DEF	 HELLO_WORLD                                ; conditional includes
/**
<pre>
    ---------------------------------------------------------------------------------------------   <br/>
    Source file name:  hello_world.inc                                                              <br/>
    Object name:       hello_world                                                                  <br/>
    Program Type:      ccl program                                                                  <br/>
    Program purpose:   Show ccl lexer functionality.                                                <br/>
                                                                                                    <br/>
    Special Notes:                                                                                  <br/>
    Usage:                                                                                          <br/>
    ---------------------------------------------------------------------------------------------   <br/>
    RELEASES                                                                                        <br/>
    ---------------------------------------------------------------------------------------------   <br/>
    Date        Mod  Name       Description                                                         <br/>
    ----------  ---  ---------  ----------------------------------------------------------------    <br/>
    2020-06-14  001  me         Initial Release                                                     <br/>
    ---------------------------------------------------------------------------------------------   <br/>
</pre>
 */


/* ---------------------------------------------------------------------------------------------
* INCLUDE FILES
* ---------------------------------------------------------------------------------------------
*/
%i cclsource:some_other_file.include

/* ---------------------------------------------------------------------------------------------
  * DECLARED RECORDS, use camelCase
  * ---------------------------------------------------------------------------------------------
  */

record someRequest(
    1 commands_list[*]
        2 command_name = vc
        2 command_arguments = vc
        2 product_name = vc
        2 server_name = vc
) with protect

record someReply(
    1 response = vc
    1 status_data[1]
        2 status = vc
        2 subeventstatus[*]
            3 ErrorDescription = vc
            3 OperationName = vc
            3 OperationStatus = vc
            3 TargetObjectName = vc
) with protect


/* ---------------------------------------------------------------------------------------------
 * Standard Opening Statements
 * ---------------------------------------------------------------------------------------------
 */
set stat = initrec(someRequest)
set stat = initrec(someReply)


/* ---------------------------------------------------------------------------------------------
 * Subroutine Definitions
 * ---------------------------------------------------------------------------------------------
 */


/**
    Do some hello world multiplication

    @param count    a i4 value to indicate the number of copies to return
    @param text     the text to multiply
    @return         a multiplied string
*/
subroutine (helloWorldMultiply(count = i4, text = vc) = vc)
    declare counter = i4 with protect, noconstant(0)
    declare buffer = vc with protect, noconstant(text)
    if (count > 0)
        for (counter = 1 to count)
            set buffer = build(buffer, char(13), text)
        endfor
    endif
    return(buffer)
end     ; helloWorldMultiply


%#ENDIF     ; HELLO_WORLD