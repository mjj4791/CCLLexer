/**
<pre>
    ---------------------------------------------------------------------------------------------   <br/>
    Source file name:  hello_world.prg                                                              <br/>
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
drop program hello_world go
create program hello_world


/* ---------------------------------------------------------------------------------------------
 * DEBUGGING & VERSION INFO
 * ---------------------------------------------------------------------------------------------
 */
declare PROG_START_TIME = dm12 with protect, constant(systimestamp)
; TODO: update version string for logging:
declare LAST_MOD = vc with constant("001"), private

if (not validate(DEBUG_NONE))
    declare DEBUG_NONE = i4 with protect, constant(0)
endif
if (not validate(DEBUG_ALL))
    declare DEBUG_ALL = i4 with protect, constant(1)
endif
if (not validate(DEBUG_FLAG))
    ; TODO: before submitting, set flag to 0:
    ; Debug settings are turned on or off with DEBUG_FLAG
    declare DEBUG_FLAG = i2 with protect, constant(1)
endif
if (DEBUG_FLAG != DEBUG_NONE)                       ; debug settings dependant on DEBUG_FLAG
    ;set message noinformation                      ; Suppress display tree information
    ;set trace nocost                               ; Suppress CCL cost information
    set trace rdbdebug
    set trace rdbbind
    set trace rdbbind2
    ;set trace rdbdebug1
    set trace rdbdebug2
    ;set trace RECPERSIST
    ;set trace DEBUGCLASS
    ;set trace ERROR
endif                                               ; debug settings dependant on DEBUG_FLAG


/* ---------------------------------------------------------------------------------------------
 * INCLUDE FILES
 * ---------------------------------------------------------------------------------------------
 */
%i hello_world.inc  ; include the accompanying inc file

/* ---------------------------------------------------------------------------------------------
 * DECLARED SUBROUTINES
 * ---------------------------------------------------------------------------------------------
 */

/* ---------------------------------------------------------------------------------------------
 * DECLARED CONSTANTS, in capitals
 * ---------------------------------------------------------------------------------------------
 */
declare HELLO_WORLD_TEXT = vc with protect, constant("Hello World!")


/* ---------------------------------------------------------------------------------------------
 * DECLARED VARIABLES, use camelCase
 * ---------------------------------------------------------------------------------------------
 */
declare i2Value = i2 with protect, noconstant(0)
declare i4Value = i4 with protect, noconstant(12)
declare vcValue = vc with protect, noconstant("")
declare dq8Value = dq8 with protect, noconstant(cnvtdatetime(curdate, curtime3))

/* ---------------------------------------------------------------------------------------------
 * DECLARED RECORDS, use camelCase
 * ---------------------------------------------------------------------------------------------
 */
record helloWorldRecord (
    1   message = vc
    1   cur_dt_tm = dq8
    1   flag = i2
    1   count = i4
    1   lines[*]
        2 line = vc
) with protect

/* ---------------------------------------------------------------------------------------------
 * Standard Opening Statements
 * ---------------------------------------------------------------------------------------------
 */

/* ---------------------------------------------------------------------------------------------
 * Main Code Block
 * ---------------------------------------------------------------------------------------------
 */
subroutine (main(null) = null)
    if (validate(helloWorldMultiply))
        set vcValue = helloWorldMultiply(i4Value, HELLO_WORLD_TEXT)

        ; store retuned value into record:
        set helloWorldRecord->flag = 1
        set helloWorldRecord->cur_dt_tm = dq8Value
        set helloWorldRecord->count = i4Value
        set helloWorldRecord->message = vcValue
    endif

    if (helloWorldRecord->flag)
        call echo(build("Message: ", helloWorldRecord->message))
        call echorecord(helloWorldRecord)
    endif

    return(null)
end ; main

call echo(build2(CURREF, " ---- START Script: ", curprog, ":", LAST_MOD, " ----"))
call main(null)


/* ---------------------------------------------------------------------------------------------
 * Subroutine Definitions
 * ---------------------------------------------------------------------------------------------
 */



/* ---------------------------------------------------------------------------------------------
 * END OF PROGRAM - Standard Closing Statements
 * ---------------------------------------------------------------------------------------------
 */
#exit_script
    /* Log start of program with its version */
    call echo(build2(CURREF, " ---- STOP Script: ", curprog, ":", LAST_MOD,
        " ---- Total time in seconds:", timestampdiff(systimestamp, PROG_START_TIME)))

end
go
;execute hello_world ^MINE^ go
